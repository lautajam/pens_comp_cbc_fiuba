"""
Obtener una palabra e imprimir la cantidad de letras.
"""

def cantidad(palabra):
    cant_letras = len(palabra)
    return cant_letras

palabra = input("Ingrese una palabra por favor: ")

print(cantidad(palabra))