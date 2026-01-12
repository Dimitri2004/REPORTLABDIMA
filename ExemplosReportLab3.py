# EXEMPLO CANVAS

from reportlab.pdfgen import canvas

# Tupla que guarda texto que mostrará
texto = ('Este texto é para exemplo',
         'da utilización de canvas',
         'para usar con texto.',
         'Alongo o texto',
         'para ter mais frases',
         ' e notar a diferencia')

# Objeto canvas que genera el pdf
obxCanvas = canvas.Canvas("3ºtextoCanvas.pdf")

# Modificaciones del texto que se añadirá
obxTexto = obxCanvas.beginText()
obxTexto.setTextOrigin(100,500)
obxTexto.setFont("Courier",16)

# Para añadir el texto en el pdf ordenado
for linha in texto:
    obxTexto.moveCursor(20,15)
    obxTexto.textLine(linha)
    obxTexto.setFillColorRGB(0.2,0,0.6)

# Añade otro texto de un color mas claro
obxTexto.setFillGray(0.5)
textoLongo = """Outro texto con varias
                liñas incorporadas,
                con retornos de carro \nincluidos."""
# Con textLines nos permite recoger el texto con retornos te carro, salto de linea, etc.
obxTexto.textLines(textoLongo)

# Modifica la posición del nuevo texto introducido sin modificar las del anterior
obxTexto.setTextOrigin(20,300)

# Modifica el tipo de letra del texto según las que la importación canvas incluye
for tipo_letra in obxCanvas.getAvailableFonts():
    obxTexto.setFont(tipo_letra,16)
    obxTexto.textLine("Texto de exemplo coa fonte: "+ tipo_letra)
    # Coloca el texto de manera escalonada
    obxTexto.moveCursor(20,15)

# Añade otro texto con sus configuraciones
obxTexto.setTextOrigin(20,800)
#obxTexto.setFillColorRGB(0.2, 0, 0.6) # Otra forma de poner color al texto
obxTexto.setFillColor('pink',1) # En vez de poner color con números se pone con nombre
obxTexto.setFont('Helvetica-BoldOblique',12)
for linha in texto:
    obxTexto.moveCursor(20,15)
    obxTexto.textOut(linha)

obxTexto.moveCursor(-60 , 15)
espazoCaracteres = 0
for linha in texto:
    obxTexto.setCharSpace(espazoCaracteres)
    obxTexto.textLine("Espazo %s: %s:" % (espazoCaracteres,linha))
    espazoCaracteres += 1

obxTexto.setTextOrigin(20, 550)
obxTexto.setCharSpace(1)
obxTexto.setWordSpace(8)
obxTexto.textLines(textoLongo)

# Pinta el texto por pantalla (ambos textos)
obxCanvas.drawText(obxTexto)

# Configuraciones para que se muestre todo  correctamente en el pdf
obxCanvas.showPage()
obxCanvas.save()