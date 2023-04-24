# Una librería tiene un sistema que guarda los nombres de todos los libros que tienen en una lista de la siguiente forma: [“El principito”, “It”, “Sherlock Holmes”...]. Se quiere saber cuántos libros repetidos tienen. Hacer código que imprima para cada título, cuántos ejemplares hay.

lista_libros = ["El gran Gatsby", "Cien años de soledad", "1984", "Matar a un ruiseñor", 
                "Las aventuras de Tom Sawyer", "La sombra del viento", "Los pilares de la Tierra", 
                "El código Da Vinci", "El nombre de la rosa", "El psicoanalista", 
                "Harry Potter y la piedra filosofal", "Las aventuras de Tom Sawyer",                "Harry Potter y el prisionero de Azkaban", "Harry Potter y el cáliz de fuego", "Harry Potter y la orden del fénix", "Harry Potter y el misterio del príncipe", "Harry Potter y las reliquias de la muerte", "It", "It", "It", "Festín de cuervos", "Danza de dragones", "It", "El resplandor", "La niebla", "Carrie", "La cúpula", "El fugitivo", "El alquimista", "Los pilares de la Tierra", "It", "El club de la pelea", "Harry Potter y la piedra filosofal", "El extraño caso del Dr. Jekyll y Mr. Hyde", "Drácula", "Frankenstein", "Los pilares de la Tierra", "Los miserables", "La isla del tesoro", "Robinson Crusoe", "Don Quijote de la Mancha", "Harry Potter y la piedra filosofal", "El principito", "Harry Potter y la piedra filosofal", "It", "Las aventuras de Tom Sawyer", "Las aventuras de Alicia en el país de las maravillas"]

def libros_repetidos(lista_libros):
    for libro in lista_libros:
        cantidad = lista_libros.count(libro)
        print("De", libro, "hay:", cantidad)

libros_repetidos(lista_libros)