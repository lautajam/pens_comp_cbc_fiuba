
def maquina_juegutes(precio):
    fichas = 0
    while fichas < precio:
        print("Ingrese", precio, "fichas para comenzar")
        letra = input()
        if letra == "f" or letra == "F":
          fichas += 1
          pass
    print("¡A jugar!")
    pass

precio = int(input("Ingrese el número de fichas que cuesta el juego: "))

maquina_juegutes(precio)