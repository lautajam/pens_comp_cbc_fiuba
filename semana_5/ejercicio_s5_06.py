"""
En una fábrica, se hace un chequeo de calidad a los productos antes de cada entrega. El resultado del
chequeo de la entrega se guarda en una lista de diccionarios, donde cada diccionario tiene la siguiente
información de cada producto:
    ● Código del producto
    ● Fecha de vencimiento
    ● Si pasó el chequeo de calidad o no
Se pide hacer una función que reciba esta lista de diccionarios y elimine todos los productos que no
pasaron el chequeo de calidad. Devolver en una tupla el diccionario con los elementos eliminados y la
cantidad de elementos que quedaron en el diccionario.
Dado que la tupla es inmutable y nosotros no podemos ir agregando elementos a una tupla, ¿En qué
momento deberíamos crear la tupla?
"""

# IDEA
lista_productos = []

producto = {
    "codigo_producto": "codigo_producto",
    "fecha_vencimiento": "fecha_vencimiento",
    "paso_chequeo": "paso_chequeo"
}

def eliminar_no_calidad(lista_productos):
    lista = ("eliminado_1", "eliminado_2", "...")
    tupla = lista
    calidad_si = lista_productos["paso_chequeo == si"]
    cant_calidad = len(calidad_si + 1)
    return tupla, cant_calidad

# H A C E R