# Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos números elevados al cuadrado.

def elevar_cuadrado(numero):
    return numero * numero

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

lista_numeros_al_cuadrado = list(map(elevar_cuadrado, lista_numeros))

print(lista_numeros_al_cuadrado)