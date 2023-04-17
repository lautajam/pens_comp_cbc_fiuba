"""
Crear una función que reciba un número entero e imprima los números primos entre 0 y el número
ingresado.
AYUDA: un número es primo cuando solamente es divisible por sí mismo y por 1, es decir que para ver
si es primo hay que ver que el módulo (%) de ese número con los anteriores hasta el 1 (sin incluirlo) sea
distinto de 0, o sea que no sea divisible.
"""

def es_primo(numero):
    for num in range(1, (numero + 1)):
      primo = True
      for n in range(2, num):
        if(num % n == 0):
          primo = False
      if(primo):
        print(num, "es primo")

numero = int(input("Ingrese un numero por favor: "))

es_primo(numero)