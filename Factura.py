#Archivo que genera una factura pdf identica a la de img.png usando ReportLab y Platypus
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os
from decimal import Decimal

# Colores inspirados en la imagen
DARK_GREEN = colors.HexColor('#234d20')
MEDIUM_GREEN = colors.HexColor('#6aa85a')
LIGHT_GREEN = colors.HexColor('#e6f2e8')

# Intentar registrar una fuente TrueType (si están disponibles), si no usar fuentes estándar
FONT_REG = {
    'regular': 'Helvetica',
    'bold': 'Helvetica-Bold',
}
try:
    base_dir = os.path.dirname(__file__)
    def find_font(name):
        candidates = [os.path.join(base_dir, name), name]
        for c in candidates:
            if os.path.isfile(c):
                return c
        return None

    dejavu = find_font('DejaVuSans.ttf')
    dejavu_b = find_font('DejaVuSans-Bold.ttf')
    if dejavu:
        pdfmetrics.registerFont(TTFont('DejaVuSans', dejavu))
        FONT_REG['regular'] = 'DejaVuSans'
    if dejavu_b:
        pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', dejavu_b))
        FONT_REG['bold'] = 'DejaVuSans-Bold'
except Exception:
    pass

# Crear estilos personalizados
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CompanyName', parent=styles['Heading1'], fontName=FONT_REG['bold'], fontSize=32, textColor=DARK_GREEN))
styles.add(ParagraphStyle(name='CompanyInfo', parent=styles['Normal'], fontName=FONT_REG['regular'], fontSize=10, textColor=DARK_GREEN))
styles.add(ParagraphStyle(name='InvoiceTitleRight', parent=styles['Heading2'], fontName=FONT_REG['bold'], fontSize=18, textColor=DARK_GREEN, alignment=2))
styles.add(ParagraphStyle(name='InvoiceInfo', parent=styles['Normal'], fontName=FONT_REG['regular'], fontSize=10, alignment=2))
styles.add(ParagraphStyle(name='TableHeader', parent=styles['Normal'], fontName=FONT_REG['bold'], fontSize=11, alignment=1, textColor=colors.white))
styles.add(ParagraphStyle(name='Small', parent=styles['Normal'], fontName=FONT_REG['regular'], fontSize=9))
styles.add(ParagraphStyle(name='Bold', parent=styles['Normal'], fontName=FONT_REG['bold']))
styles.add(ParagraphStyle(name='TotalBox', parent=styles['Normal'], fontName=FONT_REG['bold'], fontSize=14, textColor=colors.white, alignment=1))


def draw_decor(canvas, doc):
    """Dibuja la barra lateral, encabezado y pie de página en el canvas para que coincida con la imagen."""
    canvas.saveState()
    width, height = A4
    # Barra lateral izquierda: un rectángulo estrecho y otro claro
    bar_x = doc.leftMargin - 15*mm
    canvas.setFillColor(DARK_GREEN)
    canvas.rect(bar_x,  height - 20*mm, 8*mm, 12*mm, fill=1, stroke=0)  # pequeño rect superior oscuro
    canvas.setFillColor(LIGHT_GREEN)
    canvas.rect(bar_x, 20*mm, 8*mm, height - 60*mm, fill=1, stroke=0)  # rectangular central
    canvas.setFillColor(DARK_GREEN)
    canvas.rect(bar_x, 10*mm, 8*mm, 6*mm, fill=1, stroke=0)  # rect inferior

    # Título superior derecho (FACTURA SIMPLIFICADA)
    canvas.setFont(FONT_REG['bold'], 18)
    canvas.setFillColor(DARK_GREEN)
    canvas.drawRightString(width - doc.rightMargin, height - 25*mm, 'FACTURA SIMPLIFICADA')

    # Línea horizontal de pie y texto centrado
    y_line = 32*mm
    canvas.setStrokeColor(colors.black)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, y_line, width - doc.rightMargin, y_line)
    canvas.setFont(FONT_REG['regular'], 10)
    canvas.setFillColor(DARK_GREEN)
    canvas.drawCentredString(width/2, y_line - 8*mm, 'GRACIAS POR SU CONFIANZA')

    canvas.restoreState()


# Funciones auxiliares de formato
def format_number(n, decimals=2):
    """Devuelve número con decimales y coma como separador: 3.20 -> '3,20'"""
    try:
        v = Decimal(n).quantize(Decimal('1.' + '0'*decimals))
    except Exception:
        v = Decimal(str(n))
    s = f"{v:.{decimals}f}"
    return s.replace('.', ',')


def format_currency(n):
    """Formatea cantidad para mostrar en la factura: si es entero muestra sin decimales, si no con 2 decimales, usando coma."""
    try:
        v = Decimal(n).quantize(Decimal('0.01'))
    except Exception:
        v = Decimal(str(n)).quantize(Decimal('0.01'))
    if v == v.quantize(Decimal('1')):
        # entero
        s = f"{int(v)}"
    else:
        s = f"{v:.2f}"
    return s.replace('.', ',')


def format_price_short(n):
    """Formatea precios para la columna 'Importe' como en la imagen: 3.20 -> '3,2', 5.00 -> '5'"""
    try:
        v = Decimal(n).quantize(Decimal('0.01'))
    except Exception:
        v = Decimal(str(n)).quantize(Decimal('0.01'))
    s = f"{v:.2f}".replace('.', ',')
    # quitar ',00' o un cero final después de la coma
    if s.endswith(',00'):
        return s[:-3]
    if s.endswith('0'):
        return s[:-1]
    return s


# Función que construye la factura
def create_invoice(filename='Factura.pdf', company=None, client=None, invoice_meta=None, items=None, tax_rate=Decimal('0.21')):
    """Genera un PDF de factura con diseño inspirado en img.png.
    company: dict con keys name, address, phone, email, logo_path (opcional)
    client: dict con keys name, address
    invoice_meta: dict con keys number, date
    items: lista de dicts con keys description, qty, unit_price (Decimal o convertible)
    """
    if company is None:
        company = {
            'name': 'Nombre de tu Empresa',
            'address': 'Dirección\nCiudad y País\nCIF/NIF',
            'phone': 'Teléfono',
            'email': 'mail@example.com',
            'logo_path': None
        }
    if client is None:
        client = {
            'name': 'Cliente Ejemplo',
            'address': 'Dirección cliente\nCP Ciudad'
        }
    if invoice_meta is None:
        invoice_meta = {'number': 'A0001', 'date': 'DD/MM/AAAA'}
    if items is None:
        items = [
            {'description': 'Producto 1', 'qty': 5, 'unit_price': Decimal('3.20')},
            {'description': 'Producto 2', 'qty': 3, 'unit_price': Decimal('2.10')},
            {'description': 'Producto 3', 'qty': 76, 'unit_price': Decimal('2.90')},
            {'description': 'Producto 4', 'qty': 23, 'unit_price': Decimal('5.00')},
            {'description': 'Producto 5', 'qty': 3, 'unit_price': Decimal('4.95')},
            {'description': 'Producto 6', 'qty': 2, 'unit_price': Decimal('6.00')},
        ]

    doc = SimpleDocTemplate(filename, pagesize=A4,
                            rightMargin=20*mm, leftMargin=30*mm,
                            topMargin=20*mm, bottomMargin=30*mm)
    elements = []

    # Encabezado: nombre grande a la izquierda y logo/texteo a la derecha
    left = []
    left.append(Paragraph(company.get('name'), styles['CompanyName']))
    left.append(Spacer(1, 4*mm))
    left.append(Paragraph('<i>Dirección</i>', styles['CompanyInfo']))
    left.append(Paragraph(company.get('address').replace('\n', '<br/>'), styles['CompanyInfo']))
    left.append(Spacer(1, 6*mm))

    right = []
    # Si hay logo, colocarlo; si no, texto "Logo de la Empresa"
    logo_path = company.get('logo_path')
    if logo_path and os.path.isfile(logo_path):
        try:
            img = Image(logo_path, width=50*mm, height=30*mm)
            right.append(img)
        except Exception:
            right.append(Paragraph('Logo de la Empresa', styles['InvoiceTitleRight']))
    else:
        right.append(Paragraph('Logo de la Empresa', styles['InvoiceTitleRight']))
    right.append(Spacer(1, 6*mm))
    right.append(Paragraph(f'<b>Fecha Emisión</b>\t{invoice_meta.get("date")}', styles['InvoiceInfo']))
    right.append(Paragraph(f'<b>Número de Factura</b>\t{invoice_meta.get("number")}', styles['InvoiceInfo']))

    header_table = Table([[left, right]], colWidths=[100*mm, 70*mm])
    header_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    elements.append(header_table)
    elements.append(Spacer(1, 8*mm))

    # Tabla de items: Descripción | Importe | Cantidad | Total
    data = []
    data.append([Paragraph('Descripción', styles['TableHeader']), Paragraph('Importe', styles['TableHeader']), Paragraph('Cantidad', styles['TableHeader']), Paragraph('Total', styles['TableHeader'])])
    subtotal = Decimal('0.00')
    for it in items:
        qty = Decimal(str(it.get('qty', 0)))
        unit = Decimal(str(it.get('unit_price', '0.00')))
        line_total = (qty * unit).quantize(Decimal('0.01'))
        subtotal += line_total
        data.append([it.get('description'), format_price_short(unit), f"{int(qty)}", f"{format_currency(line_total)} €"])

    table = Table(data, colWidths=[90*mm, 30*mm, 30*mm, 30*mm], hAlign='LEFT')
    ts = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_GREEN),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (1,1), (2,-1), 'CENTER'),
        ('ALIGN', (3,1), (3,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.white),
        ('BOX', (0,0), (-1,-1), 0.5, DARK_GREEN),
        ('FONTNAME', (0,0), (-1,0), FONT_REG['bold']),
        ('FONTNAME', (0,1), (-1,-1), FONT_REG['regular']),
        ('FONTSIZE', (0,0), (-1,-1), 10),
    ])
    # Alternar color de filas
    for i in range(1, len(data)):
        bg = LIGHT_GREEN if i % 2 == 1 else colors.whitesmoke
        ts.add('BACKGROUND', (0, i), (-1, i), bg)
    table.setStyle(ts)
    elements.append(table)
    elements.append(Spacer(1, 8*mm))

    # Totales: recuadro verde con TOTAL a la derecha
    tax = (subtotal * Decimal(str(tax_rate))).quantize(Decimal('0.01'))
    total = (subtotal + tax).quantize(Decimal('0.01'))

    total_table = Table([[Paragraph('<b>TOTAL</b>', styles['TotalBox']), Paragraph(f"{format_currency(total)} €", styles['TotalBox'])]], colWidths=[40*mm, 40*mm], hAlign='RIGHT')
    total_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), DARK_GREEN),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 0, colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))

    # Alinearlo a la derecha con un contenedor
    wrapper = Table([[None, total_table]], colWidths=[110*mm, 60*mm])
    wrapper.setStyle(TableStyle([('ALIGN', (1,0), (1,0), 'RIGHT'), ('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    elements.append(wrapper)
    elements.append(Spacer(1, 12*mm))



    # Construir con el dibujo decorativo en cada página
    doc.build(elements, onFirstPage=draw_decor, onLaterPages=draw_decor)
    return filename


if __name__ == '__main__':
    create_invoice()
