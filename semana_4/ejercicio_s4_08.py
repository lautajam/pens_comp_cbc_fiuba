"""
Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.
    a. Crear una tupla para cada país que contenga su nombre, su capital y el continente donde se
    encuentra.
    b. Guardar las tuplas en una lista.
    c. Hacer una función que reciba por parámetros la lista, e imprima la información de cada país
    con el siguiente formato:
        País: <nombre>
        Capital: <capital>
        Continente: <continente>
    Por ejemplo:
    País: Japón
    Capital: Tokio
    Continente: Asia
"""

# A)
pais_1 = ("Argentina", "Buenos Aires", "America")
pais_2 = ("Francia", "Paris", "Europa")
pais_3 = ("Japon", "Tokio", "Asia")
pais_4 = ("Alemania", "Berlin", "Europa")
pais_5 = ("Peru", "Lima", "America")

# B)
lista_paises = [
    pais_1,
    pais_2,
    pais_3,
    pais_4,
    pais_5
]

# C)

def impresion_paises(lista_paises):
    for pais in lista_paises:
        print("Pais:", pais[0])
        print("Capital:", pais[1])
        print("Continente:", pais[2])

impresion_paises(lista_paises)