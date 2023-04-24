"""
Se tiene la siguiente lista de palabras: [“entender”, “pueden”, “humanos”, “los”, “que”, “código”,
“escriben”, ”programadores”, “buenos”, “Los”, “entiende.”, “computadora”, “una”, “que”, “código”,
“escribe”, “tonto”, “Cualquier”]. Hacer una función que reciba una lista, y devuelva un string uniendo
las palabras desde el final de la lista hasta el principio con un “ ” (espacio) entre cada una, para formar la frase.
"""


lista_palabras = ['entender', 'pueden', 'humanos', 'los', 'que', 'código', 'escriben', 'programadores', 'buenos', 'Los', 'entiende.', 'computadora', 'una', 'que', 'código', 'escribe', 'tonto', 'Cualquier']


def frase(lista_palabras):
    lista_palabras.reverse()
    frase = ""
    for palabra in lista_palabras:
        frase = frase + " " + palabra
    return frase.strip() + "."

print(frase(lista_palabras))