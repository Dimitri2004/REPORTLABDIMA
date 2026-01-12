# Doc con Platypus

from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.rl_settings import showBoundary

guion = []

follaEstilo = getSampleStyleSheet()

cabeceira = follaEstilo["Heading4"]

cabeceira.pageBreakBefore = 0
cabeceira.backColor = colors.lightblue

paragrafo = Paragraph("CABECEIRA DO DOCUMENTO", cabeceira)
guion.append(paragrafo)

texto = "Texto incluido no documento, e que forma o contido" * 1000

corpoTexto = follaEstilo['BodyText']
corpoTexto.fontSize = 12
paragrafo2 = Paragraph(texto,corpoTexto)
guion.append(paragrafo2)

guion.append(Spacer(0,30))
imaxe = Image("box-pixilart.png",width=400,height=400)
guion.append(imaxe)

doc = SimpleDocTemplate("4º ExemplosPlatypus.pdf", pagesize = A4,showBoundary = 1)
doc.build(guion)
