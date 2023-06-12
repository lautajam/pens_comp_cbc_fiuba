"""
Una profesora tiene una lista de diccionarios para guardar las notas que sacaron sus alumnos en el
último parcial que tomó. Cada uno de esos diccionarios tiene el nombre del alumno, su apellido, su dni
y la nota que sacó.
a. Hacer una función que reciba este diccionario, y guarde las notas en un archivo csv, llamados
notas.csv
b. Tiempo después de guardar las notas, la profesora quiso saber la cantidad de alumnos que
aprobaron. Hacer una función que lea el archivo creado en el ejercicio anterior, y devolver la
cantidad de alumnos aprobados (su nota es mayor a 4).
"""

alumnos = [
    {"nombre": "Juan", "apellido": "Gómez", "dni": "12345678", "nota": 8},
    {"nombre": "María", "apellido": "López", "dni": "23456789", "nota": 2},
    {"nombre": "Pedro", "apellido": "Martínez", "dni": "34567890", "nota": 7},
    {"nombre": "Ana", "apellido": "Rodríguez", "dni": "45678901", "nota": 10},
    {"nombre": "Luis", "apellido": "García", "dni": "56789012", "nota": 6},
    {"nombre": "Laura", "apellido": "Fernández", "dni": "67890123", "nota": 5},
    {"nombre": "Carlos", "apellido": "Pérez", "dni": "78901234", "nota": 3},
    {"nombre": "Sofía", "apellido": "Hernández", "dni": "89012345", "nota": 9},
    {"nombre": "Diego", "apellido": "Gutiérrez", "dni": "90123456", "nota": 6},
    {"nombre": "Valentina", "apellido": "Navarro", "dni": "01234567", "nota": 1},
    {"nombre": "Andrés", "apellido": "Silva", "dni": "12345098", "nota": 7},
    {"nombre": "Camila", "apellido": "Rojas", "dni": "23456109", "nota": 1},
    {"nombre": "Mateo", "apellido": "Vargas", "dni": "34567210", "nota": 2},
    {"nombre": "Julia", "apellido": "Mendoza", "dni": "45678321", "nota": 4},
    {"nombre": "Gabriel", "apellido": "Soto", "dni": "56789432", "nota": 6}
]

archivo = open("semana_6/archivos/notas.csv", "r+", encoding="utf-8")

#   A)
def pasarCsv(alumnos):
    nombres = []
    apellidos = []
    dni = []
    notas = []
    espacio = ["\n"]

    for alumno in alumnos:
        nombres.append(alumno["nombre"] + ";")
        apellidos.append(alumno["apellido"] + ";")
        dni.append(alumno["dni"] + ";")
        notas.append(str(alumno["nota"]) + ";")
        
    archivo.writelines(nombres + espacio + apellidos + espacio + dni + espacio + notas + espacio)

pasarCsv(alumnos)

#   B)
def ver_aprobados(archivo):
    archivo_rescatado = archivo.readlines()
    archivo.close()

    notas_crudo = archivo_rescatado[3]
    notas = notas_crudo.split(";")
    notas.pop()

    contador = 0
    for nota in notas:
        if int(nota) >= 4:
            contador += 1
    return contador

aprobados = ver_aprobados(archivo)

print("La cantidad de aprobados son:", aprobados)
