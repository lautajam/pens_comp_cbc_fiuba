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

shampoo = {
"codigo_producto": "SH001",
"fecha_vencimiento": "05/2024",
"paso_chequeo": False
}

galletas = {
"codigo_producto": "GA002",
"fecha_vencimiento": "12/2023",
"paso_chequeo": True
}

jabon_manos = {
"codigo_producto": "JM003",
"fecha_vencimiento": "08/2025",
"paso_chequeo": False
}

lapices = {
"codigo_producto": "LP004",
"fecha_vencimiento": "N/A",
"paso_chequeo": False
}

botella_agua = {
"codigo_producto": "BW005",
"fecha_vencimiento": "N/A",
"paso_chequeo": True
}

yogur = {
"codigo_producto": "YG006",
"fecha_vencimiento": "06/2023",
"paso_chequeo": True
}

detergente = {
"codigo_producto": "DT007",
"fecha_vencimiento": "10/2024",
"paso_chequeo": False
}

cepillo_dientes = {
"codigo_producto": "CD008",
"fecha_vencimiento": "N/A",
"paso_chequeo": True
}

lamina_papel = {
"codigo_producto": "LP009",
"fecha_vencimiento": "N/A",
"paso_chequeo": False
}

cuchillo_cocina = {
"codigo_producto": "CK010",
"fecha_vencimiento": "N/A",
"paso_chequeo": True
}

lista_productos = [shampoo, galletas, jabon_manos, lapices, botella_agua, yogur, detergente, cepillo_dientes, lamina_papel, cuchillo_cocina]

def eliminar_no_calidad(lista_productos):
    lista_eliminados = []
    cant_calidad_si = 0
    for producto in lista_productos:
        if producto["paso_chequeo"] == False:
            lista_eliminados.append(producto)
        else:
            cant_calidad_si += 1
    tupla_eliminados = lista_eliminados
    return tupla_eliminados, cant_calidad_si

tupla_eliminados,cant_calidad_si = eliminar_no_calidad(lista_productos)

print("Eliminados:", tupla_eliminados)
print("Pasaron calidad:", cant_calidad_si)
