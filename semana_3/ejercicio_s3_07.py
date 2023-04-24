"""Se tienen letras para representar las estaciones del año:
  ● V para verano
  ● O para otoño
  ● I para invierno
  ● P para primavera
Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es
decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a
ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O,
B, V e I."""

def estacion(letra):
    if letra.lower() == "v":
      print("Verano")
    elif letra.lower() == "o":
      print("Otoño")
    elif letra.lower() == "i":
      print("Invierno")
    elif letra.lower() == "p":
      print("Primavera")
    else: 
       print("Error")

#Pruebas
estacion("A")
estacion("P")
estacion("O")
estacion("B")
estacion("V")
estacion("I")
estacion(letra = input("Ingrese una letra de una estacion (V: VERANO, O: OTOÑO, I: INVIERNO, o P: PRIMAVERA: "))