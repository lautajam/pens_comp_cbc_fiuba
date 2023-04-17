#Se quiere hacer un programa para enseñar a unos niños a contar. Crear una función que reciba un
#número entero e imprima por pantalla los números del 1 hasta ese número con la estructura de control
#iterativa for.


def aprender_contar(numero):
    for num in range(1, (numero + 1)):
        print(num)

numero = int(input("Ingrese un numero para aprender a contar hasta ese numero: "))
aprender_contar(numero)