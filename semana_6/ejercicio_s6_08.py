""" 
Santi le fue mostrando colores a sus amigos y cada amigo le fue diciendo si le gusta o no. Guardó cada
respuesta en un .csv de la siguiente manera: nombre;color;le gusta, pero se dió cuenta que no es una
forma muy práctica de guardarlo, así que lo quiere cambiar. Hacer un programa que lea el archivo y lo
transforme en un archivo .txt. Es decir que si se tiene un archivo csv de la siguiente forma:
Agus;verde;si
Tomi;violeta;no
Manu;marrón;no
Ana;azul;si
Carla;rojo;no
Luis;amarillo;si
Marta;naranja;no
Pablo;gris;no
Laura;blanco;no
Juan;negro;no
El archivo .txt tiene que quedar así:
A Agus si le gusta el verde
A Tomi no le gusta el violeta
A Manu no le gusta el marrón
A Ana si le gusta el azul
A Carla no le gusta el rojo
A Luis si le gusta el amarillo
A Marta no le gusta el naranja
A Pablo no le gusta el gris
A Laura no le gusta el blanco
A Juan no le gusta el negro
"""

archivo = open("semana_6/archivos/colores.csv", "r", encoding="utf-8")
colores_crudo = archivo.readlines()
archivo.close()

def transformar(colores):
    colores = colores.strip("\n")
    colores = colores.split(";")
    return colores

colores = list(map(transformar, colores_crudo))

print(colores)

def frasear(colores):
    frases = []
    for color in colores:
        frase = "A " + color[0] + " " + color[2] + " le gusta el " + color[1]
        frases.append(frase)
    return frases

frases = frasear(colores)

print(frases)

archivo = open("semana_6/archivos/colores.csv", "w", encoding="utf-8")
for frase in frases:
    archivo.writelines(frase+"\n")
archivo.close()