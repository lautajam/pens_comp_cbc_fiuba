
archivo = open("C:/Users/Lautaro/Desktop/python/ejercicios_variados_parcial_2/archivos/datos_personas.csv", "r", encoding="utf-8")
datos_personas_crudo = archivo.readlines()
archivo.close()

# print(datos_personas_crudo)

datos_personas = []

# Crea la lista con los datos generada por el CSV, quitando los ; y los \n
def crear_lista(datos_personas_crudo):
    datos_persona = []
    for datos in datos_personas_crudo:
        datos = datos.strip("\n")
        datos = datos.split(",")
        datos_persona.append(datos)
    return datos_persona

datos_personas = crear_lista(datos_personas_crudo)

# print(datos_personas)

# Separo las keys para el dataframe de la lista de datos
keys = datos_personas[0]

datos_lista = datos_personas[1:]

valores = []

# Se paro cada uno de los datos para luego poder ponerlos en sus respectivas listas
def separar_lista(lista):
    valores = []
    for datos in lista:
        for dato in datos:
            valores.append(dato)
    return valores

valores = separar_lista(datos_lista)

# print(valores)

# Crea las listas de cada uno de los apartados del dataframe
def unir(lista):
    nombres, edad, oficio, nacionalidad, tipo_sangre, contador = [], [], [], [], [], 0
    for dato in lista:
        if contador == 0:
            nombres.append(dato)
        if contador == 1:
            edad.append(dato)
        if contador == 2:
            oficio.append(dato)
        if contador == 3:
            nacionalidad.append(dato)
        if contador == 4:
            tipo_sangre.append(dato)
            contador = 0
            continue
        contador += 1
    return nombres, edad, oficio, nacionalidad, tipo_sangre

# nombres, edad, oficio, nacionalidad, tipo_sangre = unir(valores)

# print(nombres)
# print(edad)
# print(oficio)
# print(nacionalidad)
# print(tipo_sangre)

# values = [nombres, edad, oficio, nacionalidad, tipo_sangre]

values = unir(valores)

# Crea al dataframe
datos = dict(zip(keys, values))

print(datos)