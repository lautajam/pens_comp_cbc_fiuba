"""
Se tiene un archivo csv que contiene información sobre el stock de una librería. Se guarda por cada
línea, el nombre del producto, el código, el precio por unidad y el stock actual, es decir:
nombre;código;precio;stock
Un posible ejemplo de este archivo es el siguiente:
lapiceras;34512;50;120
cuadernos;41611;500;130
sacapuntas;62812;30;210
…
Se pide:
a. Leer el archivo y mostrarlo por pantalla con el siguiente formato:
Nombre producto: lapiceras
Código producto: 34512
Precio por unidad: 50
Stock: 120
Nombre producto: cuadernos
Código producto: 41611
Precio por unidad: 500
Stock: 130
b. Hacer una función que reciba un diccionario que describa una línea del archivo y lo agregue, es
decir que si se recibe un diccionario del tipo
{
“nombre”: “hojas A4”,
“código”: 35662,
“precio”: 600,
“stock”: 45
}

"""

archivo = open("semana_6/archivos/productos.csv", "r", encoding="utf-8")
texto_crudo = archivo.readlines()
archivo.close()

def arreglar(texto):
    texto = texto.strip("\n")
    texto = texto.split(";")
    return texto

inventario_lista= list(map(arreglar, texto_crudo))

#   A)

for producto in inventario_lista:
    print("Nombre producto:", producto[0])
    print("Código producto:", producto[1])
    print("Precio por unidad:", producto[2])
    print("Stock:", producto[3])

#   B)

#FALTA HACER#