""""
Hacer una lista con 5 nombres, y realizar las siguientes actividades con la misma:
    a. Cambiar el último elemento de la lista y cambiar el último nombre por “Juan”. ¿Cómo podría
    saber cuál es el último elemento si no sé la longitud?
    b. Devolver el nombre que esté a dos posiciones del final.
    c. Recorrer la lista e imprimir cada nombre por pantalla.
    d. Imprimir por pantalla la lista con 3 repeticiones, usar el operador repetición (*).
"""

nombres = [
    "Esteban",
    "Maria",
    "Pedro",
    "Filiperto",
    "Susana"
]

# A)
print(nombres)
nombres[4] = 12
nombres[3] = "Juan"
print(nombres)
print("------------")

# B)
print(nombres[len(nombres) - 3])

print("------------")

# C)
for nombre in nombres:
    print(nombre)

print("------------")

# D)
print(nombres * 3)