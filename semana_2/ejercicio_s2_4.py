#Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad #tenía el usuario en el año ingresado.

año_nacimiento = int(input("Ingrese su año de nacimiento: "))
año_x = int(input("Ingrese un año para saber su edad en ese año: "))

edad = "Su edad es/será " + str(año_x - año_nacimiento) if (año_nacimiento <= año_x) else "No había nacido"

print(edad)