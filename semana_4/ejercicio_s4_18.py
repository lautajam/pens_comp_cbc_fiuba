"""
Agustina está jugando a las cartas con sus amigos. A ella le gusta tener las cartas de su mano bien
ordenadas. Esto significa que cada vez que tiene que agarrar una nueva carta, la quiere agregar a su
mano en el lugar indicado para no romper el orden.
Si se tiene una lista de enteros ordenadas de mayor a menor. Hacer una función que según esta lista
inserte un nuevo entero, manteniendo el orden.
¿En este caso nos conviene usar append?
"""

lista_numeros =[1,2,3,4,5,6,7,8,9,10] 

def ordenar_numeros(lista_numeros):
    while 1:
        numero = int(input("Ingrese un numero entero: "))
        if(numero == 123456789):
            break
        lista_numeros.append(numero)
        lista_numeros.sort()

ordenar_numeros(lista_numeros)

print(lista_numeros)
