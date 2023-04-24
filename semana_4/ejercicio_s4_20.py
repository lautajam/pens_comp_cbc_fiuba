"""
Manuel y su pareja armaron una lista numerada con las actividades de mantenimiento de la casa.
Decidieron dividirse las tareas, a Manuel le tocó hacer todas las actividades con número par.
Hacer una función que reciba una lista de enteros, y devuelva otra lista que solamente contenga
números pares.
"""

enteros = list(range(1, 51))

def pares(enteros):
    num_pares = []
    for numero in enteros:
        if (numero % 2 == 0):
            num_pares.append(numero)
    return num_pares

lista_pares = pares(enteros)

print(lista_pares)