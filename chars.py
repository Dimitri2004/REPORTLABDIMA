from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Spacer
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

d2 = Drawing(400,200)

graficoLinhas=HorizontalLineChart() # crea o gráfico de liñas
graficoLinhas.x=30
graficoLinhas.y=50
graficoLinhas.height=125
graficoLinhas.width=350
graficoLinhas.data=datos # datos do gráfico
graficoLinhas.categoryAxis.categoryNames = lendaDatos # nomes das categorías
graficoLinhas.categoryAxis.labels.boxAnchor='n' # ancoraxe das etiquetas
graficoLinhas.valueAxis.valueMin=0 # valor mínimo do eixo de valores
graficoLinhas.valueAxis.valueMax=100 # valor máximo do eixo de valores
graficoLinhas.valueAxis.valueStep=20 # paso do eixo de valores
graficoLinhas.lines[0].strokeWidth=2 # grosor da liña
graficoLinhas.lines[0].symbol = makeMarker('FilledCircle') # símbolo para os puntos da liña 0
#graficoLinhas.lines[0][7].symbol=makeMarker('FilledTriangle')
graficoLinhas.lines[1].strokeWidth=1.5 # grosor da liña
d2.add(graficoLinhas)




d3 = Drawing(400,200) # crea o gráfico de pastel
graficoPastel = Pie()
graficoPastel.x = 65
graficoPastel.y = 15
graficoPastel.height= 170
graficoPastel.width = 170
graficoPastel.data = [10,20,30,40,50] # datos do gráfico
graficoPastel.labels = ['Oppo','Pixel','Galaxy','iPhone','Xiaomi']  # etiquetas do gráfico
graficoPastel.slices.strokeWidth = 0.5 # grosor da liña dos anacos
graficoPastel.slices[3].popout = 10  # destaca o anaco 3
graficoPastel.slices[3].strokeDashArray = [7,3] # liña discontinua no anaco destacado
graficoPastel.slices[3].labelRadius = 1.75 # distancia da etiqueta ao centro do gráfico
graficoPastel.slices[3].fontColor = colors.red # cor da etiqueta do anaco destacado
graficoPastel.sideLabels = 1 # coloca as etiquetas fóra do gráfico

colores=[colors.blue,colors.red,colors.green,colors.yellow,colors.palegreen]
for i, cor in enumerate(colores):
    graficoPastel.slices[i].fillColor=cor


lenda = Legend() # crea a lenda do gráfico de pastel (listado de colores e valores)
lenda.colorNamePairs = [(graficoPastel.slices[i].fillColor,
                         (graficoPastel.labels[i][0:20], '%0.2f' % graficoPastel.data[i]))
                        for i in range(len(graficoPastel.data))] # engade os elementos á lenda
lenda.x=370 # posición horizontal da lenda
lenda.y=5 # posición da lenda
lenda.fontName='Helvetica' # tipo de fonte
lenda.fontSize = 7 # tamaño da fonte
lenda.boxAnchor = 'n' # dibuja a lenda dende arriba cara abaixo
lenda.columnMaximum = 5 # número máximo de elementos por columna
lenda.strokeWidth =1 # grosor do cadro da lenda
lenda.strokeColor=colors.black # cor do cadro da lenda
lenda.deltax = 20 # espazo entre columnas
lenda.deltay = 10 # espazo entre filas
lenda.autoXPadding = 5 # espazo entre o cadro e o texto
lenda.yGap = 0 # espazo entre filas
lenda.dxTextSpace = 5 # espacio entre o símbolo e o texto
lenda.alignment='right' # 'right' o 'left'
lenda.dividerLines = 7 # activa as liñas divisorias
lenda.dividerOffsY = 5.5 # desprazamento vertical das liñas divisorias
lenda.subCols.rpad = 10 # espazo á dereita do símbolo
d3.add(lenda) # engade a lenda ao gráfico
d3.add(graficoPastel) # engade o gráfico ao dibujo





doc = SimpleDocTemplate("ExemploGrafico.pdf",pagesize=A4) # crea o documento PDF
doc.build([d,Spacer(20,20),d2,Spacer(20,20),d3]) # engade os gráficos ao documento con espazos entre eles