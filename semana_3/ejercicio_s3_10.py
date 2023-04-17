#Crear una función que simule un cumpleaños: que dado un entero imprima “Que los cumplas feliz” esa
#cantidad de veces.

def cumpleaños(numero):
    for num in range(1, (numero + 1)):
        print("Que los cumplas feliz n°", num)

numero = int(input("Ingrese un numero por favor: "))

cumpleaños(numero)