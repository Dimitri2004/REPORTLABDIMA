from reportlab.platypus import Table, SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


guion = [] # esto es una lista que contendrá os elementos do documento

tit = ['','','FACTURA SIMPLIFICADA',''] # título da factura
cab = ['Nombre de tu Empresa','','Logo de la Empresa',''] # cabeceira da factura
dic = ['Dirección',''] # dirección da empresa
loc = ['Ciudad y País',''] # localización da empresa
NIF = ['CIF/NIF','','Fecha Emisión','DD/MM/AAAA'] # NIF e data de emisión
tel = ['Teléfono','','Número de Factura','A0001'] # teléfono e número de factura
mail = ['Mail',''] # correo electrónico
spc = [''] # fila en branco para espaciado
desc =['Descripción','Importe','Cantidad','Total'] # cabeceira da táboa de produtos
p1 = ['Producto 1','3,2','5','16,00'] # produto 1
p2 = ['Producto 2','2,1','3','6,30'] # produto 2
p3 = ['Producto 3','2,9','76','220,40'] # produto 3
p4 = ['Producto 4','5','23','115,00'] # produto 4
p5 = ['Producto 5','4,95','3','14,85'] # produto 5
p6 = ['Producto 6','6','2','12,00'] # produto 6
final = ['','','TOTAL','385€'] # fila final co total da factura
# creación da táboa coa lista de listas
taboa = Table([ # definición das filas da táboa
    tit, #
    cab,
    dic,
    loc,
    NIF,
    tel,
    mail,
    spc,
    desc,
    p1,
    p2,
    p3,
    p4,
    p5,
    p6,
    spc,
    final
]) # crea la tabla

taboa.setStyle([('SPAN',(2,0),(-1,0)), # estilo
                ('SPAN',(2,1),(-1,1)), #
                ('ALIGN',(2,0),(-1,1),'RIGHT'), #
                ('TEXTCOLOR',(0,0),(-1,6),colors.darkgreen), #
                ('FONT',(0,0),(-1,8),"Helvetica-Bold"), #
                ('SIZE',(0,0),(-1,1),18), #
                ('FONT',(-1,4),(-1,6),"Helvetica"), #
                ('ALIGN',(0,8),(-1,15),'CENTER'), #
                ('ALIGN',(-1,9),(-1,15),'RIGHT'), #
                ('BACKGROUND',(0,8),(-1,8),colors.darkgreen), #
                ('TEXTCOLOR',(0,8),(-1,8),colors.white),#
                ('BACKGROUND',(0,9),(-1,14),colors.lightgreen), #
                ('BACKGROUND',(2,16),(-1,16),colors.darkgreen), #
                ('TEXTCOLOR',(2,16),(-1,16),colors.white), #
                ('INNERGRID', (0,8), (-1, 15), 0.5, colors.white), # liñas internas da táboa
                ('FONT',(2,16),(-1,16),"Helvetica-Bold",12), # pon o total en negrita
                ('ALIGN',(2,16),(-1,16),"CENTER"), # aliña o total ao centro
                ('TOPPADDING',(1,1),(-1,1),20), # espaciado extra na táboa
                ('TOPPADDING',(0,2),(-1,2),20), # espaciado extra na táboa
                ]) # estilo da táboa
guion.append(taboa) # engade a táboa ao guion do documento



doc = SimpleDocTemplate("FacturaEjemplo.pdf",pagesize=A4) # crea o documento

doc.build(guion) # constrúe o documento co guion definido