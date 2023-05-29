"""
Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar,
imprimiendo un mensaje por pantalla en cada caso. Es decir, el output esperado sería:
> El número 1 es impar.
> El número 2 es par.
…
> El número 20 es par.
"""

num = 0

while num <= 20:
    if num % 2 == 0:
        print(num, "es par")
    else:
        print(num, "es impar")
    num += 1