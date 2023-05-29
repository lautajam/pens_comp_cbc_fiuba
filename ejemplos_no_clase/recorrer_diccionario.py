numeros = {
    "pares": ((2,4,6),(8,10)),
    "primos": ((1,3,5),(9,11))
}

for valores in numeros.values():
    for tupla_1 in valores:
        for tupla_2 in tupla_1:
                print(tupla_2)