"""
Un chef está armando una lista de supermercado con todos los ingredientes que hay que comprar. Sólo
quiere agregar un ingrediente a la lista si no lo escribió antes, así no tiene repetidos.
Hacer un programa que inserte un nuevo elemento en una lista de strings, solamente si el elemento
que se desea insertar no se encuentra en la lista.
"""

lista_compra = []

def agregar_elemento(lista_compra):
    while 1:
        producto = input("Ingrese un elemento que quiera comprar: ")
        if(producto.lower() == "x"):
            return
        if(producto in lista_compra):
            while 1:
                producto = input("Este producto ya está en lista de compra, ingrese otro: ")
                if(producto in lista_compra):
                    continue
                else:
                    break
        lista_compra.append(producto)

agregar_elemento(lista_compra)

print(lista_compra)