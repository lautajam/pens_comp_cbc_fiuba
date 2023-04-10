# Obtener una palabra, borrarle todas las ‘a’ e imprimirla por pantalla.

palabra = input("Ingrese una palabra: ")

nueva_palabra = palabra.replace("a", "")

print("La palabra", palabra, "sin las 'a' es", nueva_palabra)