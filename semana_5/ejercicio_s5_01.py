"""
En una escuela se quiere tener un sistema para guardar la información de sus estudiantes para tener
mejor organizado sus datos.
    a. Crear un diccionario que sirve para representar a una persona en este contexto, pensar en las
    características que se consideren más relevantes para identificar a una persona (su nombre,
    DNI, edad, etc).
    b. Agregar al diccionario creado, un campo que sea otro diccionario y sirva para guardar el curso
    del estudiante y sus características (año, división, orientación, etc).
    c. Teniendo una lista de diccionarios de estudiantes, buscar en la lista la persona con mayor edad 
    e imprimirla por pantalla.
"""

alumno_1 = {'nombre': 'Laura',
            'apellido': 'Díaz',
            'edad': 16,
            'dni': 33213217,
            'telefono': 6065384942,
}

academico_1 = {'año': '1ro', 'division': 'C', 'orientacion': 'Artes'}

alumno_1["academico"] = academico_1

alumno_2 = {'nombre': 'Pedro',
            'apellido': 'Martínez',
            'edad': 19,
            'dni': 41246503,
            'telefono': 9074004028,
}

academico_2 = {'año': '2do', 'division': 'D', 'orientacion': 'Ciencias Naturales'}

alumno_2["academico"] = academico_2

alumno_3 = {'nombre': 'Lucas',
            'apellido': 'Hernández',
            'edad': 15,
            'dni': 32501320,
            'telefono': 7994202173,
}

academico_3 = {'año': '1ro', 'division': 'C', 'orientacion': 'Humanidades'}

alumno_3["academico"] = academico_3

alumno_4 = {'nombre': 'Sofía',
            'apellido': 'Hernández',
            'edad': 15,
            'dni': 89729046,
            'telefono': 3684247397,
}

academico_4 = {'año': '5to', 'division': 'D', 'orientacion': 'Ciencias Naturales'}

alumno_4["academico"] = academico_4

alumno_5 = {'nombre': 'Carla',
            'apellido': 'García',
            'edad': 19,
            'dni': 71142621,
            'telefono': 9936048644,
}

academico_5 = {'año': '3ro', 'division': 'C', 'orientacion': 'Sociales'}

alumno_5["academico"] = academico_5

alumno_6 = {'nombre': 'Jorge',
            'apellido': 'Álvarez',
            'edad': 20,
            'dni': 69529460,
            'telefono': 7038240311,
}

academico_6 = {'año': '3ro', 'division': 'B', 'orientacion': 'Sociales'}

alumno_6["academico"] = academico_6

alumno_7 = {'nombre': 'Ana', 
            'apellido': 'Rodríguez',
            'edad': 21,
            'dni': 30697821,
            'telefono': 1119200975,
}

academico_7 = {'año': '6to', 'division': 'D', 'orientacion': 'Humanidades'}

alumno_7["academico"] = academico_7

alumnos = [alumno_1, alumno_2, alumno_3, alumno_4, alumno_5, alumno_6, alumno_7]

def buscar_edad_grande(alumnos):
    edad = 0
    alumno_edad_max = {}
    for alumno in alumnos:
        if edad < alumno["edad"]:
            edad = alumno["edad"]
            alumno_edad_max = alumno
    return alumno_edad_max

print(buscar_edad_grande(alumnos))
