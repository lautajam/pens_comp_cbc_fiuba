#Crear una función que una un string y un entero.

def union(cadena, entero):
    resultado = cadena + str(entero)
    return resultado

cadena = input("Ingrese una palabra por favor: ")
entero = int(input("Ingrese un numero: "))

print("La union es:", union(cadena, entero))