"""
Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de
ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con
ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del
usuario, y no solo para 100?.
"""

num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: "))

suma = num_1 + num_2

numero = int(input("Ingrese un limite: "))

if suma < numero:
    falta = numero - suma
    print("Falta", falta)
elif suma >= numero:
    print("Llega a 100")