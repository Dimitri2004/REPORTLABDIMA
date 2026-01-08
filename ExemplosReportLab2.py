from reportlab.graphics.shapes import Image, Drawing
from reportlab.graphics import renderPDF
from reportlab.lib.pagesizes import A4

# Los objetos a introducir, se introducen en una lista
guion = []

# Posicionamiento de una imagen y tamaño
imaxe = Image(20,100,32,32,"box-pixilart.png")
imaxe2 = Image(60,100,32,32,"box-pixilart.png")

# "Cuadro" donde se añadirá la imagen creada
debuxo = Drawing(300,32)
debuxo2 = Drawing(300,102)
debuxo3 = Drawing()
# Añade la imagen al cuadro
debuxo.add(imaxe)

debuxo2.add(imaxe2)
debuxo.translate(150,350)

debuxo3.add(imaxe)
debuxo3.rotate(33)
debuxo3.translate(200,200)

# Se añade al contenedor de objetos
guion.append(debuxo)
guion.append(debuxo2)
guion.append(debuxo3)

# Representa el tamaño de una hoja formato A4
folla = Drawing(A4[0], A4[1])
print(A4)

for elemento in guion:
    folla.add(elemento)
    renderPDF.drawToFile(folla,"2ºexemploDrawing.pdf")