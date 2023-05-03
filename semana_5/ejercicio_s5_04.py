"""
Sol tiene una lista de diccionarios donde guarda todas las películas que vió. La información que tiene
para cada una es: el nombre de la serie, año en que salió, y la puntuación que le puso del 1 al 10. Hace
mucho que quiere que Tomás empiece a ver las películas que ella considera que son las mejores que
vio.
Hacer una función que reciba el diccionario de las películas que vió Sol, y que devuelva una nueva lista
de diccionarios donde sólo estén las películas que tienen puntaje mayor a 7.
"""

peli_1 = {"nombre": "The Shawshank Redemption", "año": 1994, "puntaje": 6}
peli_2 = {"nombre": "The Godfather", "año": 1972, "puntaje": 9}
peli_3 = {"nombre": "The Dark Knight", "año": 2008, "puntaje": 8}
peli_4 = {"nombre": "The Godfather: Part II", "año": 1974, "puntaje": 9}
peli_5 = {"nombre": "12 Angry Men", "año": 1957, "puntaje": 5}
peli_6 = {"nombre": "Schindler's List", "año": 1993, "puntaje": 2}
peli_7 = {"nombre": "The Lord of the Rings: The Return of the King", "año": 2003, "puntaje": 1}
peli_8 = {"nombre": "Pulp Fiction", "año": 1994, "puntaje": 6}
peli_9 = {"nombre": "The Good, the Bad and the Ugly", "año": 1966, "puntaje": 7}
peli_10 = {"nombre": "Fight Club", "año": 1999, "puntaje": 8}

pelis_sol = [peli_1, peli_2, peli_3, peli_4, peli_5, peli_6, peli_7, peli_8, peli_9, peli_10]

pelis_tomi = []

def llenar_lista_tomi(pelis_sol, pelis_tomi):
    for peli in pelis_sol:
        if peli["puntaje"] > 7:
            pelis_tomi.append(peli)
    return pelis_tomi

pelis_tomi.append(llenar_lista_tomi(pelis_sol, pelis_tomi))

print(pelis_tomi)