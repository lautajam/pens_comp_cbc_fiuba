
s = "hola putos"

print(s.index("hola"))

print("*************************************")

def cuadrados(s):
    return s * s

numeros = [1, 2, 3, 4, 5]
map_object = map(cuadrados, numeros)

print(numeros)
print(list(map_object))

print("*************************************")

def pares(n):
    if n % 2 == 0:
        return True
    else:
        return False

numeros = [1, 2, 3, 4, 5]
filter_object = filter(pares, numeros)

print(list(filter_object))