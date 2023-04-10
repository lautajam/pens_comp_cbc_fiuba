"""Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
● la suma de ambos números
● la resta de ambos números
● la multiplicación de ambos números
● la división entera de ambos números
● el resto
Más adelante podríamos crear nuestra propia calculadora :)
"""

entero_1 = int(input("Por favor, ingrese un número entero: "))
entero_2 = int(input("Por favor, ingrese otro número entero: "))

suma = entero_1 + entero_2
resta = entero_1 - entero_2
multiplicacion = entero_1 * entero_2
division = entero_1 / entero_2
resto = entero_1 % entero_2

print("Los numeros ingresados fueron: ", entero_1, " y ",  entero_2)
print("La suma de ambos fue: ", suma)
print("La resta de ambos fue: ", resta)
print("La multiplicacion de ambos fue: ", multiplicacion)
print("La division de ambos fue: ", division)
print("La resto de ambos fue: ", resto)
