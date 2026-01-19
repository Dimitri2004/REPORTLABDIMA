from reportlab.graphics.charts.barcharts import  VerticalBarChart
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.shapes import Drawing
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4

d = Drawing(400,200)
titulo=Label()
titulo.setOrigin(200,190)
titulo.setText("Porcentaxe contratados/aprobados")
d.add(titulo)

lendaLabel=Label()
lendaLabel.setOrigin(10,100)
lendaLabel.angle=90
lendaLabel.setText("Porcentaxe")
d.add(lendaLabel)

datos = [(13.3,8,14.3,25,33.3,37.5,21.1,28.6,45.5,38.1,54.6,36,42.3)]
lendaDatos = ['11/12','12/13','13/14','14/15','15/16','16/17','17/18','18/19','19/20','20/21','21/22','22/23','23/24','25/25']

graficoBarras = VerticalBarChart()

# Posición inicial
graficoBarras.x = 50
graficoBarras.y = 50

#Altura anchura
graficoBarras.height = 125
graficoBarras.width = 300

# Datos
graficoBarras.data = datos

graficoBarras.valueAxis.valueMin = 0
graficoBarras.valueAxis.valueMax = 70

graficoBarras.valueAxis.valueStep = 10

graficoBarras.categoryAxis.labels.boxAnchor = 'ne'
graficoBarras.categoryAxis.labels.angle = 15

graficoBarras.categoryAxis.categoryNames =lendaDatos
graficoBarras.barSpacing = 5
d.add(graficoBarras)

doc = SimpleDocTemplate("6ºExemplosGraficos.pdf",pagesize = A4)

doc.build([d])
