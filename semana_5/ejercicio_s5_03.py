"""
Se representa un ticket de supermercado como una lista de diccionarios, donde cada diccionario tiene
la siguiente información:
    ● Nombre del producto
    ● Precio por unidad
    ● Cantidad
Se pide hacer una función que reciba el ticket y devuelva el monto total a pagar.
"""

ticket = []

def llenar_ticket():
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_por_unidad = int(input("Ingrese precio del producto por unidad: "))
    cantidad = int(input("Ingrese la cantidad de producto comprado: "))
    producto = {
        "nombre_producto": nombre_producto,
        "precio_por_unidad": precio_por_unidad,
        "cantidad": cantidad
    }
    return producto

while 1:
    ingreso = input("¿Tiene productos que ingresar? Si o no: ")
    if ingreso.lower() == "no":
        precio_total = 0
        for producto in ticket:
            precio_total = precio_total + producto["precio_por_unidad"] * producto["cantidad"]
        print("El precio total del producto es:", precio_total)
        print(ticket)
        break
    ticket.append(llenar_ticket())