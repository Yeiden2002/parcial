import qrcode
import os
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import date
from datetime import datetime
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_codigo_rastreo():
    return str(random.randint(1000000, 9999999))
today = date.today()
now = datetime.now()

ruta = "C:/Users/monse/OneDrive/Escritorio/EXAMEN PYTHON/"


fecha_actual = datetime.now()
fecha_entrega = fecha_actual + timedelta(days=5)

codigo_rastreo = generar_codigo_rastreo()

informacion_qr = f"Emmanuel Hinojosa Esparza   Código: {codigo_rastreo}\nFecha: {fecha_entrega.strftime('%Y-%m-%d')}"
qr_code = qrcode.make(informacion_qr)

if not os.path.exists(ruta):
    os.makedirs(ruta)
nombre_imagen = os.path.join(ruta, "ema.png")
qr_code.save(nombre_imagen)

def generar_ticket(nombre, direccion, correo, productos, cantidades, precios_unitarios, precios_totales, codigo_rastreo, fecha_entrega):
    c = canvas.Canvas(ruta + "fina21.pdf", pagesize=A4)
    c.setFont('Helvetica', 20)
    c.drawString(25, 800, "AEROCOSTAL")

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "TICKET")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50,730,"**************************************************************************")
    c.drawString(50, 700, "Nombre: " + nombre)
    c.drawString(50, 680, "Dirección: " + direccion)
    c.drawString(50, 660, "Correo electrónico: " + correo)


    c.setFont("Helvetica-Bold", 12)
    c.drawString(50,630,"**************************************************************************")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(210,600, "Datos de los productos ")
    c.setFont('Helvetica', 14)
    c.drawString(50, 570, "Nombre del producto")
    c.drawString(200, 570, "Cantidad")
    c.drawString(270, 570, "Precio unitario")
    c.drawString(370, 570, "Precio total")

    y_position = 540
    for i in range(len(productos)):
        c.drawString(50, y_position, productos[i])
        c.drawString(200, y_position, str(cantidades[i]))
        c.drawString(270, y_position, "$" + str(precios_unitarios[i]))
        c.drawString(350, y_position, "$" + str(precios_totales[i]))
        y_position -= 20

    total = sum(precios_totales)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 350, "Total: $" + str(total))

    

    
    qr_data = fecha_entrega + " - " + codigo_rastreo
    
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_file = "2121.png"
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_file)

    print("Ticket generado exitosamente.")
    c.drawImage(nombre_imagen,205,170,170,170)
    c.save()
if __name__ == "__main__":
    nombre = input("Nombre de la persona: ")
    direccion = input("Dirección: ")
    correo = input("Correo electrónico: ")

    productos = []
    cantidades = []
    precios_unitarios = []
    precios_totales = []

    n = int(input("¿Cuántos productos quieres agregar? "))
    for i in range(n):
        productos.append(input("Nombre del producto {}: ".format(i + 1)))
        cantidades.append(int(input("Cantidad de {}: ".format(productos[i]))))
        precios_unitarios.append(float(input("Precio unitario de {}: $".format(productos[i]))))
        precios_totales.append(cantidades[i] * precios_unitarios[i])

    codigo_rastreo = generar_codigo_rastreo()
    fecha_entrega = input("Fecha de entrega: ")

        
    
  
    generar_ticket(nombre, direccion, correo, productos, cantidades, precios_unitarios, precios_totales, codigo_rastreo, fecha_entrega)
    

