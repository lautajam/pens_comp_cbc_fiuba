"""
En un cine tienen dos archivos .txt, uno con salas y otro con nombres de películas. Se sabe que en la
sala de una fila del archivo se va a transmitir la película de la misma fila del archivo de películas. Se pide
leer los dos archivos, y crear un nuevo archivo csv que tenga el nuevo formato sala;pelicula
Por ejemplo si se tienen los siguientes archivos:
(salas.txt) (peliculas.txt)
D2 Megamente
F1 Rápidos y furiosos
E4 El padrino

El nuevo archivo deberá quedar:
(funciones.csv)
D2;Megamente
F1;Rápidos y furiosos
E4;El padrino
"""

archivo_funciones = open("semana_6/archivos/funciones.csv", "w", encoding="utf-8")

archivo_salas = open("semana_6/archivos/salas.txt", "r", encoding="utf-8")
archivo_peliculas = open("semana_6/archivos/peliculas.txt", "r", encoding="utf-8")

salas_crudo = archivo_salas.readlines()
salas = []
peliculas_crudo = archivo_peliculas.readlines()
peliculas = []

if len(salas_crudo) >= len(peliculas_crudo):
    indice = len(salas_crudo)

    for indice in range(0,len(salas_crudo)):
        salas.append(salas_crudo[indice].replace('\n', ''))
        peliculas.append(peliculas_crudo[indice].replace('\n', ''))

    for indice in range(0,len(salas_crudo)):
        archivo_funciones.writelines(salas[indice] + ";" + peliculas[indice] + "\n")
else:

    for indice in range(0,len(peliculas_crudo)):
        salas.append(salas_crudo[indice].replace('\n', ''))
        peliculas.append(peliculas_crudo[indice].replace('\n', ''))

    for indice in range(0,len(peliculas_crudo)):
        archivo_funciones.writelines(salas[indice] + ";" + peliculas[indice] + "\n")


# FORMA LARGA
# for sala in salas_crudo:
#     sala = sala.replace('\n', '')
#     salas.append(sala)

# for pelicula in peliculas_crudo:
#     pelicula = pelicula.replace('\n', '')
#     peliculas.append(pelicula)