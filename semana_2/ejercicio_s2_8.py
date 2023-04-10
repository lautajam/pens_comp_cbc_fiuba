#Crear una función que reciba un entero y que retorne el resto y el cociente.

def division(entero_1, entero_2):
    cociente = entero_1 / entero_2
    resto = entero_1 % entero_2
    return cociente, resto

entero_1 = int((input("Ingrese un entero, por favor: ")))
entero_2 = int((input("Ingrese un entero, por favor: ")))

cociente, resto = division(entero_1, entero_2)

print("El cociente de", entero_1, "/", entero_2, "es:", cociente)
print("El resto de", entero_1, "/", entero_2, "es:", resto)