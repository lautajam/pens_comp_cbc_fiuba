"""Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de
ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con
ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.

#Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del
usuario, y no solo para 100?."""

def determina(num_1, num_2):
    if (num_1 + num_2 >= 100):
      print("La suma de", num_1, "+", num_2, "llega a 100. Da", num_1 + num_2)
    else:
       print("La suma de", num_1, "+", num_2, "no llega a 100. Lo que falta es:", (100 - (num_1 + num_2)))

num_1 = int(input("Ingrese un numero por favor: "))

num_2 = int(input("Ingrese otro numero por favor: "))

determina(num_1, num_2)


"""
#EXTRA

def determina(num_1, num_2, total):
    if (num_1 + num_2 >= total):
      print("La suma de", num_1, "+", num_2, "llega a", total, "\nDa", num_1 + num_2)
    else:
       print("La suma de", num_1, "+", num_2, "no llega a", total, "\nLo que falta es:", (total - (num_1 + num_2)))

num_1 = int(input("Ingrese un numero por favor: "))

num_2 = int(input("Ingrese otro numero por favor: "))

total = int(input("Ingrese un numero total por favor: "))

determina(num_1, num_2, total)

"""
    