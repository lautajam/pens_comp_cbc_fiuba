"""
Se quiere hacer un sistema en la facultad para que un alumno pueda ir guardando las materias que va
haciendo. Para eso, crear una función que le pregunte al usuario la materia que quiere almacenar, e ir
guardando la información en una lista hasta que ingrese una 'X'.
AYUDA: para guardar elementos nuevos en una lista usamos el método append()
"""

materias = []

def agregar_materias(materias):
    while 1:
        materia = input("Ingrese una de sus materias, por favor: ")
        if (materia.lower() == "x"):
            break
        materias.append(materia)

agregar_materias(materias)

print(materias)