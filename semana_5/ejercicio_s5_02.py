"""
En un vivero se guardan las plantas en una lista de diccionario con la siguiente información: especie, si
necesita luz solar o no, y el precio. (OBSERVACIÓN: ¿Qué tipo de dato nos permitía guardar si algo es
verdad o no?). Ahora se necesita un sistema que guarde las plantas a medida que van llegando. Se pide
hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva y agregue
esa planta a la lista de diccionarios.
"""

lista_plantas = []

def guardar_plantas():
    especie = input("Ingrese la especie de la planta: ")
    necesita_luz = input("¿Necesita luz? Si o no: ")
    if necesita_luz.lower() == "si":
        necesita_luz = True
    else:
        necesita_luz = False
    precio = input("Ingrese precio de la planta: ")
    planta = {
        "especie": especie,
        "necesita_luz": necesita_luz,
        "precio": precio
    }
    return planta

while 1:
    ingreso = input("¿Quiere ingresar una planta? Si o no: ")
    if ingreso.lower() == "no":
        for planta in lista_plantas:
            print(planta)
        break
    lista_plantas.append(guardar_plantas())