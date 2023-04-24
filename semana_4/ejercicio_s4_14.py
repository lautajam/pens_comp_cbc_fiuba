# Hacer una función que reciba un string y que imprima solamente los caracteres que sean vocales.

letras_vocales = ("a", "e", "i", "o", "u")

def vocales(cadena):
    vocal = ""
    for letra in cadena:
        if (letra in letras_vocales):
            vocal = vocal + " " + letra
    print(vocal.strip())

vocales("supercalifragilisticoespialidoso")
