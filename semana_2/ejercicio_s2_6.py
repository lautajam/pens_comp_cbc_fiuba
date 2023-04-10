#Crear una función que reciba un número y muestre el anterior y el siguiente.

def secuencia(numero):
    print("El numero anterior es:", (numero - 1))
    print("El siguiente anterior es:", (numero + 1))

numero = int(input("Por favor ingrese un numero: "))

secuencia(numero)