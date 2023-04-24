"""
Un matrimonio está organizando una fiesta y tiene que armar una lista de invitados. Cada uno tiene su propia tupla y guarda en ella a todos los que quiere invitar.
    a) Si alguien cancela tienen que sacarlo de la tupla.
    Hacer una función que reciba la tupla y un nombre , y devuelva una nueva tupla sin el nombre pasado
    por parámetro. Las tuplas son inmutables, entonces ¿Cómo podemos hacer para “eliminar” un elemento de una tupla?
    b) Cuando ya tienen a todos los invitados tienen que juntar sus tuplas.
    Hacer una función que a partir de dos tuplas cree una sola que sea la combinación de ambas tuplas.
"""

invitados_el = ("Ana", "Beto", "Carlos", "Diana", "Enrique", 
                "Federico", "Gina", "Hugo", "Iván", "Julia", 
                "Karla", "Luis", "Marta", "Nicolás", "Olga", 
                "Pablo", "Quirino", "Ramona", "Sofía", "Tomás")

invitados_ella = ("Adriana", "Bruno", "Carmen", "Diego", "Esther", 
                  "Francisco", "Gabriela", "Isabel", "Juan", "Karen", 
                  "Leonardo", "María", "Nacho", "Oscar", "Patricia", 
                  "Raúl", "Sara", "Teresa", "Valentina", "Ximena")

# A)
def cancela(invitados, nombre):
    if (nombre in invitados):
        invitados = list(invitados)
        invitados.remove(nombre)
        invitados = tuple(invitados)
        return invitados

print("----------INVITADOS ELLA----------")
print(invitados_ella)
print("----------INVITADOS NUEVOS ELLA----------")
print("----------------SIN ISABEL---------------")
invitados_nuevo_ella = cancela(invitados_ella, "Isabel")
print(invitados_nuevo_ella)
print("----------INVITADOS EL----------")
print(invitados_el)
print("----------INVITADOS NUEVOS EL----------")
print("-----------------SIN IVAN----------------")
invitados_nuevo_el = cancela(invitados_el, "Iván")
print(invitados_nuevo_el)

# B)
def juntar_tuplas(invitados_el, invitados_ella):
    invitados_el = list(invitados_el)
    invitados_ella = list(invitados_ella)
    invitados = invitados_el + invitados_ella
    invitados.sort()
    tuple(invitados)
    return(invitados)

invitados_final = juntar_tuplas(invitados_nuevo_el, invitados_nuevo_ella)

print("----------INVITADOS TOTALES---------")
print(invitados_final)