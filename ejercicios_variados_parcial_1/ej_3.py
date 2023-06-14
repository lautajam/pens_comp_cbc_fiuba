"""
Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
    ● la suma de ambos números
    ● la resta de ambos números
    ● la multiplicación de ambos números
    ● la división entera de ambos números
    ● el resto
"""
num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: "))

suma = num_1 + num_2
resta = num_1 - num_2
mult = num_1 * num_2
div_entera = num_1 // num_2
resto = num_1 % num_2

print(suma, resta, mult, div_entera, resto)