"""
Se quiere guardar la información de un grupo de maratonistas. Se necesita guardar su nombre, DNI, y
todas las maratones que corrió, de la cual a su vez se quiere tener el nombre de cada una, el año, el
puesto en que salió el maratonista, y el tiempo que tardó en terminarla.
	a. Crear el diccionario que represente esta situación.
	AYUDA: Queremos guardar muchos maratonistas, y a su vez, muchas maratones para cada
	maratonista, entonces ¿Qué tipo de dato debería ser el campo que guarda todas las
	maratones? ¿Y qué tipo de dato es la maratón en sí?
	b. Teniendo una lista de diccionarios de maratonistas, ordenarlos alfabéticamente.
	c. Ordenar las maratones de cada maratonista según el tiempo que tardó en completar cada una
	de forma ascendente.
"""

# A)

maratonista_1 = {
    "nombre": "Pedro Fernandez",
    "dni": 20345487,
    "maratones":
    [["Maraton benefica", 5, 90],
     ["Tardes de maraton", 3, 80],
     ["Corrida de toros", 7, 95],
     ["MaratonX", 10, 120],
     ["McRaton", 1, 200]]
}

maratonista_2 = {
    "nombre": "Juan Rodriguez",
    "dni": 30768954,
    "maratones": [["Maraton ciudad de Buenos Aires", 5, 78],
                  ["Maraton del Fin del Mundo", 10, 145],
                  ["Maraton de los valles", 2, 60]
                  ]
}

maratonista_3 = {
    "nombre": "Laura Gutierrez",
    "dni": 40876523,
    "maratones": [["Maratón de la primavera", 9, 110],
                  ["Maratón de la costa", 6, 95],
                  ["Maratón del bosque", 1, 70]]
}

maratonista_4 = {
    "nombre": "Carlos Gonzalez",
    "dni": 50321967,
    "maratones": [["Maratón de la selva", 2, 75],
                  ["Maratón de la nieve", 7, 95],
                  ["Maratón de la montaña", 5, 90],
                  ["Maratón de la ciudad", 3, 80]]
}

maratonista_5 = {
    "nombre": "Ana García",
    "dni": 28765984,
    "maratones": [["Maratón de la primavera", 1, 70],
                  ["Maratón del invierno", 8, 100],
                  ["Maratón del mar", 3, 80]]
}

maratonista_6 = {
    "nombre": "Ricardo Alvarez",
    "dni": 40231568,
    "maratones": [["Maratón de la montaña", 5, 90],
                  ["Maratón de la lluvia", 10, 120],
                  ["Maratón del campo", 3, 80],
                  ["Maratón del viento", 7, 95]]
}

maratonista_7 = {
    "nombre": "Kiara Ramos",
    "dni": 54873625,
    "maratones": [
        ["Maratón de la primavera", 8, 100],
        ["Maratón del invierno", 5, 90],
    ]
}

maratonista_8 = {
    "nombre": "Samantha Ruiz",
    "dni": 34876654,
    "maratones": [
        ["Maraton de la Ciudad", 2, 60]
    ]
}

maratonista_9 = {
    "nombre": "Lucas Perez",
    "dni": 29567321,
    "maratones": [["Maraton del Sur", 3, 80],
                  ["Maraton por la Naturaleza", 7, 95],
                  ["Maratón del bosque", 2, 75],
                  ["Maraton del Barrio", 10, 120]]
}

maratonista_10 = {
    "nombre": "Isabel Garcia",
    "dni": 36789123,
    "maratones": [["Maraton de la Costa", 5, 90],
                  ["Maratón de la ciudad", 2, 75],
                  ["La Gran Carrera", 7, 95],
                  ["Maratón de la montaña", 4, 85]]
}

# B)

maratonistas = [maratonista_1, maratonista_2, maratonista_3, maratonista_4, maratonista_5,
                maratonista_6, maratonista_7, maratonista_8, maratonista_9, maratonista_10]

# Crea una lista con los nombres de los maratonistas
def nombres_maratonistas(maratonistas):
    list_nombres = []
    for maratonista in maratonistas:
        list_nombres.append(maratonista["nombre"])
    return list_nombres

# Crea una lista con los nombres ordenados alfabeticamente
def ordenar_nombres(maratonistas):
    list_nombres = nombres_maratonistas(maratonistas)
    list_nombres.sort()
    list_maratonistas = []
    for nombres in list_nombres:
        for maratonista in maratonistas:
            if maratonista["nombre"] == nombres:
                list_maratonistas.append(maratonista)
    return list_maratonistas

"""---PRUEBA FUNCIONAMIENTO---"""

# PRUEBA antes:
list_nombres_prueba_antes = nombres_maratonistas(maratonistas)

print("*Antes ordenar*")
print(list_nombres_prueba_antes)

# ORDENO los maratonistas
maratonistas = ordenar_nombres(maratonistas)

# PRUEBA despues:
list_nombres_prueba_Despues = nombres_maratonistas(maratonistas)

print("*Despues ordenar*")
print(list_nombres_prueba_Despues)


"""
C) *A R R E G L A R*

def lista_tiempos(maratonistas):
    tiempos = []
    for maratonista in maratonistas:
        list_tiempos = []
        for maratones in maratonista["maratones"]:
            list_tiempos.append(maratones[2])
        list_tiempos.sort()
        tiempos.append(list_tiempos)
    return tiempos

def ordenar_maratonistas_tiempos(maratonistas):
    tiempos = lista_tiempos(maratonistas)
    maratonistas_final = []
    for tiempos_maratonista in tiempos:
        for tiempo_maraton in tiempos_maratonista:
            for maratonista in maratonistas:
                for maratones in maratonista["maratones"]:
                    for maraton in maratones:
                        if maraton[2] == tiempo_maraton:
                            maratonista["maratones"][2].append(tiempo_maraton)
            maratonistas_final.append(maratonista)
    return maratonistas_final

maratonistas = ordenar_maratonistas_tiempos(maratonistas)

print(maratonistas)

tiempos = [
			[80, 90, 95, 120, 200], 
			[60, 78, 145], 
			[70, 95, 110], 
			[75, 80, 90, 95], 
			[70, 80, 100], 
			[80, 90, 95, 120], 
			[90, 100], 
			[60], 
			[75, 80, 95, 120], 
			[75, 85, 90, 95]
		]
"""
