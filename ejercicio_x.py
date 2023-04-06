def pi_pa_ti(leta):
    if letra == "r":
      print("Papel, te gané")
      pass
    elif letra == "p":
      print("Tijera, te gané")
      pass
    elif letra == "t":
      print("Piedra, te gané")
      pass
    else:
      print("NO es una letra válida")
      pass
    pass

letra = input("Elije un movimiento ('R' para piedra, 'P' para papael y 'T' pra tijera): ")

pi_pa_ti(letra)