"""
Un profesor guarda las notas del primer parcial de sus alumnos en una lista de diccionarios que guarda
la siguiente información:
    ● Nombre
    ● Apellido
    ● Intento
    ● Nota
Donde ”intento” es la instancia que está rindiendo, 1 si es la primera vez que rinde el parcial, 2 si es el primer recuperatorio y 3 si es el segundo recuperatorio.
    A) Se pide hacer una función que, dado esta lista de diccionarios, devuelva el promedio de las notas en la primera oportunidad que rindieron los alumnos.
    B) ¿Cómo harían para generalizar la función y que el intento sea parametrizable? Es decir, que no
    solamente sirve para el intento 1, sino que también pueda servir para los demás.
"""

listado_alumnos =  [
    {'nombre': 'Miguel', 'apellido': 'Fernández', 'intento': 3, 'nota': (1, 3, 10)}, 
    {'nombre': 'Sofía', 'apellido': 'Lucero', 'intento': 3, 'nota': (2, 3, 10)}, 
    {'nombre': 'Pedro', 'apellido': 'Pérez', 'intento': 1, 'nota': (4, 0, 0)}, 
    {'nombre': 'Ana', 'apellido': 'López', 'intento': 1, 'nota': (5, 0, 0)}, 
    {'nombre': 'María', 'apellido': 'García', 'intento': 2, 'nota': (1, 6, 0)}, 
    {'nombre': 'Ana', 'apellido': 'Estebanez', 'intento': 2, 'nota': (3, 5, 0)}, 
    {'nombre': 'Juan', 'apellido': 'Rodríguez', 'intento': 1, 'nota': (9, 0, 0)}, 
    {'nombre': 'Esteban', 'apellido': 'Jualto', 'intento': 3, 'nota': (2, 3, 10)}, 
    {'nombre': 'Kiko', 'apellido': 'Pertez', 'intento': 1, 'nota': (7, 0, 0)}, 
    {'nombre': 'Lautaro', 'apellido': 'Fillsho', 'intento': 2, 'nota': (0, 6, 0)}
]

# A)
def promedio_notas_primera_vuelta (listado_alumnos):
    notas = 0
    for alumno in listado_alumnos:
        notas = notas + alumno["nota"][0]
    return notas/len(listado_alumnos)

print("Promedio de notas: ", promedio_notas_primera_vuelta(listado_alumnos))

# B)
def promedio_notas (listado_alumnos):
    vuelta = int(input("¿Qué número de vuelta quiere calcular? (1, 2, 3): "))
    if vuelta > 3 or vuelta < 1:
        while 1:
            print("Ingrese un numero valido.")
            vuelta = int(input("¿Qué número de vuelta quiere calcular? (1, 2, 3): "))
            if vuelta <= 3 or vuelta >= 1:
                break
    notas = 0
    cant_alum_int = 0
    for alumno in listado_alumnos:
        if alumno["intento"] >= vuelta:
            notas = notas + alumno["nota"][vuelta - 1]
            cant_alum_int += 1
    return notas/cant_alum_int

print("Promedio de notas: ", promedio_notas(listado_alumnos))