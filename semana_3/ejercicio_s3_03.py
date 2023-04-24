#  Repetir pero para la expresión que permite saber si un número es par y menor a 10.

numero = int(input("Ingrese una numero por favor: "))

par_y_menor_10 = (numero % 2 == 0) and (numero < 10)

print(numero, "es par y menor que 10:", par_y_menor_10)