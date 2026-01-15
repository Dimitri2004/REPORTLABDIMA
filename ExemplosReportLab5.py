# Taboas Platypus

from reportlab.lib.colors import Color
from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.rl_settings import showBoundary
from reportlab.platypus import Table

imaxe = Image("box-pixilart.png",width=23,height=23)
texto = Paragraph("Libre")
h = ['HORARIO']<
cab = ['-','Luns','Martes','Mercores','Xoves','Venres','Sabado','Domingo']
actM = ['Mañán',"Cole","Correr",[imaxe,texto],'-','-','Estudar','Traballar']
actT =['Tarde','Trabalar','Clases','Clases','Clases','Traballar','Traballar','Ler']
actN = ['Noite','-','Traballar','Traballar','Traballar','-','-','-']
taboa = Table([h,cab,actM,actT,actN])
taboa.setStyle([('TEXTCOLOR',(1,-4),(7,-4),colors.red),
                ('TEXTCOLOR',(0,0),(0,3),colors.blue),
                ('BACKGROUND',(1,-4),(-1,-4), colors.lightblue),
                ('BOX',(0,0),(-1,-1),1,colors.blue),
                ('INNERGRID',(1,1),(-1,-1),0.25,colors.blue),
                ('LINEBELOW',(1,0),(7,0),0.25, colors.lightgreen),
                ('LINEAFTER', (0, 1), (0, -1), 0.25, colors.lightgreen),
                ('SPAN', (0, 0), (-1, 0)),
                ('ALIGN',(0,0),(-1,0),'CENTER')
                ])


guion = []
guion.append(taboa)

doc = SimpleDocTemplate("5º ExemplosPlatypusTablas.pdf", pagesize = A4,showBoundary = 1)
doc.build(guion)


