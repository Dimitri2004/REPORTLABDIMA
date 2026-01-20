# Doc con Platypus
from reportlab.platypus import Paragraph # parágrafos
from reportlab.platypus import Image # imaxes
from reportlab.lib.styles import getSampleStyleSheet # folla de estilos
from reportlab.graphics.charts.barcharts import VerticalBarChart # gráfico de barras
from reportlab.graphics.charts.textlabels import Label # etiquetas de texto
from reportlab.graphics.shapes import Drawing # debuxos
from reportlab.lib import colors # cor
from reportlab.platypus import SimpleDocTemplate, Spacer # espazo
from reportlab.lib.pagesizes import A4 # tamaño da páxina A4

d = Drawing(400,200)

titulo=Label() # crea o título do gráfico
titulo.setOrigin(200,250) # posición do título
titulo.setText("Porcentaxe contratados/aprobados") # texto do título
d.add(titulo) # engade o título ao gráfico

lendaLabel=Label() # crea a etiqueta do eixo Y
lendaLabel.setOrigin(10,100) # posición da etiqueta do eixo Y
lendaLabel.angle=90 # rota a etiqueta 90 graos
lendaLabel.setText("Porcentaxe") # etiqueta do eixo Y
d.add(lendaLabel) # engade a etiqueta do eixo Y

datos = [(13.3,8,14.3,25,33.3,37.5,21.1,28.6,45.5,38.1,54.6,36.0,42.3),
         (67,69,68,81,92,90,87,82,77,79,59,69,61)] # datos do gráfico
lendaDatos = ['11/12','12/13','13/14','14/15','15/16','16/17','17/18','18/19','19/20','20/21','21/22','22/23','23/24','24/25'] # nomes das categorías

graficoBarras = VerticalBarChart() # crea o gráfico de barras

graficoBarras.x = 50
graficoBarras.y = 50
graficoBarras.height = 125
graficoBarras.width = 300
graficoBarras.data = datos
graficoBarras.valueAxis.valueMin = 0
graficoBarras.valueAxis.valueMax = 70
graficoBarras.valueAxis.valueStep = 10
graficoBarras.categoryAxis.labels.boxAnchor = 'ne'
graficoBarras.categoryAxis.labels.dx = 8
graficoBarras.categoryAxis.labels.dy = -10
graficoBarras.categoryAxis.labels.angle = 30
graficoBarras.categoryAxis.categoryNames = lendaDatos
graficoBarras.groupSpacing = 10

d.add(graficoBarras)




guion = []




follaEstilo = getSampleStyleSheet() # obtén a folla de estilos predeterminada
print(follaEstilo.list()) # amosa os estilos dispoñibles
cabeceira = follaEstilo["Heading4"] # copia da cabeceira

cabeceira.pageBreakBefore = 0 # non facer salto de páxina antes
cabeceira.backColor = colors.lightblue # cor de fondo

paragrafo = Paragraph("CABECEIRA DO DOCUMENTO", cabeceira) # crea un parágrafo coa cabeceira
guion.append(paragrafo)

texto = "Texto incluido no documento, e que forma o contido" * 1000 # texto longo

corpoTexto = follaEstilo['BodyText'] # copia do estilo de corpo de texto
corpoTexto.fontSize = 12 # tamaño da fonte
paragrafo2 = Paragraph(texto,corpoTexto) # crea un parágrafo co texto e o estilo de corpo de texto
guion.append(paragrafo2)

guion.append(Spacer(0,30))# espazo vertical
imaxe = Image("box-pixilart.png",width=400,height=400) # crea a imaxe
guion.append(imaxe) # engade a imaxe ao guion

cabeceiraCursiva = follaEstilo["Heading4"]  # copia da cabeceira
cabeceiraCursiva.fontName = 'Helvetica-Oblique' # fonte cursiva
cabeceiraCursiva.fontSize = 18 # tamaño da fonte
cabeceiraCursiva.alignment = 1 # aliñado ao centro
cabeceiraCursiva.borderColor = colors.blue # cor da borda

paragrafo3 = Paragraph("Cabezeira cursiva", cabeceiraCursiva)
guion.append(paragrafo3)

guion.append(Spacer(0,20))
guion.append(d)

doc = SimpleDocTemplate("4º ExemplosPlatypus.pdf", pagesize = A4,showBoundary = 1)
doc.build(guion)


