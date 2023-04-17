# Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.

letra = input("Ingrese una letra por favor: ")

es_vocal = letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"

print(letra, "es vocal:", es_vocal)