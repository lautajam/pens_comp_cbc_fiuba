"""
Crear una función que reciba un número entero e imprima los números primos entre 0 y el número
ingresado.
"""

def primos(numero):
    for num in range(1, (numero + 1)):
        primo = True
        for n in range(2, num):
            if num % n == 0:
                primo = False
        if primo == True:
            print(num)

primos(25)