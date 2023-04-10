"""Crear un programa que le solicite al usuario un entero y determine si es par, mostrando por pantalla un mensaje que indique el resultado.
Para determinar si un número es par o impar, se puede determinar con el uso del operador %, les
dejamos a ustedes el cómo.
"""

numero = int(input("Ingrese un numero para determinar si es par o impar: "))

resto = numero % 2

print("Es par" if (resto == 0) else "Es impar")