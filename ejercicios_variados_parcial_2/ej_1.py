"""
En un hogar se quieren organizar mejor con las compras, por lo que se quiere guardar en un archivo la
lista de productos que se necesitan para la próxima vez que la familia vaya al supermercado. Se pide
hacer un programa que cree un archivo de compras.txt (Ayuda: abrir el archivo en modo w) y le
pregunte al usuario qué necesita comprar hasta que ingrese una X. Por ejemplo
> ¿Qué agrego a la lista de compras?
> Papa
> ¿Qué agrego a la lista de compras?
> Pollo
> ¿Qué agrego a la lista de compras?
> Fideos
> ¿Qué agrego a la lista de compras?
> X
El archivo tendría que estar de la siguiente forma:
Papa
Pollo
Fideos
"""

archivo = open("ejercicios_variados_parcial_2/archivos/compra.txt", "w", encoding="utf-8")

def lista_compra():
    lista_compra = []
    while True:
        compra = input("¿Qué agrego a la lista de compras? ")
        if compra.lower() == "x":
            break
        lista_compra.append(compra)
    return lista_compra

def agregar(lista_compra):
    for compra in lista_compra:
        archivo.writelines(compra + "\n")

agregar(lista_compra())