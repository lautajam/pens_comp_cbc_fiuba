""""
En un archivo llamado regalo.txt se tiene la lista de las personas que quieren participar en el regalo de
cumpleaños de Sol (en cada línea está el nombre de una persona). El encargado de organizar el regalo
es Ale, y quiere saber más información antes de ir a comprarle algo a Sol.
a. Mostrar por pantalla los nombres de las personas que quieren participar en el regalo.
b. Se sabe que quieren poner 1000 pesos por persona por regalo. Hacer una función que devuelva
cuánto dinero tiene Ale para hacerle el regalo a Sol. Es decir si se tiene un archivo de esta
forma:
Agus
Manu
Santi
Lorena
Maria
La función tiene que devolver 5000
c. Ale sabe que si participa Santi, también participa Tomi. Se pide que si Santi está en el archivo
de los nombres, se agregue también a Tomi.
"""

archivo = open("semana_6/archivos/regalo.txt", "r+")
personas_crudo = archivo.readlines()

#   A)
def trasnformar(persona):
    persona = persona.strip("\n")
    return persona

personas = list(map(trasnformar, personas_crudo))

print("Las personas que van a poner para el regalo de Sol son: ")
for persona in personas:
    print(persona)

#   B)
def plata(personas):
    dinero = len(personas) * 1000
    return dinero

cantidad_plata = plata(personas)

print("La plata que se recaudó fue: $",cantidad_plata)

#   C)
def revisar(personas):
    if "Santi" or "santi" in personas:
        personas.append("Tomi")
        archivo.writelines("\nTomi")

revisar(personas)

for persona in personas:
    print(persona)