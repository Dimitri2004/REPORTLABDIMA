from reportlab.pdfgen import canvas

# Crea un objeto canvas
# Es como una hoja o un documento
folla = canvas.Canvas("1ºprimeiroDocumento.pdf")

# Las coordenadas en las que se empieza a pintar en roportlab es en la esquina inferior izquierda (0,0)
# En reportlab se "pintan" no se "añaden"

# Ejemplo de como se "pintan" unos strings por pantalla
folla.drawString(0,0,"Posición inicial (x,y) = (0,0)")
folla.drawString(50,750,"Posición (x,y) = (50,750)")
folla.drawString(150,20, "Posición (x,y) = (150,20)")

# Permite añadir imagenes
folla.drawImage("box-pixilart.png",50,700)
folla.drawImage("equis16x216.jpg",50,650)

# Permite mostrar la página
folla.showPage()
folla.save()