"""
Obtener una palabra, borrarle todas las 'a' e imprimirla por pantalla.
"""

def modif_palabra(palabra, letra_borrar,reemplazo):
    palabra_nueva = ""
    for letra in palabra:
        if letra != letra_borrar:
            palabra_nueva += letra
        else:
            palabra_nueva += reemplazo
    return palabra_nueva

palabra = "eutanasia"
letra_borrar = "a"
reemplazo = ""

nueva_palabra = modif_palabra(palabra, letra_borrar, reemplazo)

print(nueva_palabra)