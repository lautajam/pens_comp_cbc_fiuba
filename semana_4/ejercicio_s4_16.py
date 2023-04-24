# Hacer una función que reciba dos strings, un string y un substring, es decir, que el primero contiene al segundo, se pide devolver el string habiendo eliminado el substring del mismo.

def separar(cadena, subcadena):
    longitud_sub = len(subcadena) - 1
    longitud = len(cadena) - 1
    longitud_corte = longitud - longitud_sub
    return cadena[:longitud_corte]

subcadena = ", como estás?"
cadena = "Hola amigo, como estás?"

print(cadena)

print(separar(cadena, subcadena))