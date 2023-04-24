"""Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio anterior. Ahora se
necesita una funcionalidad que permita a los niños aprender las tablas. Crear una función que reciba un
número entero e imprima por pantalla la tabla de ese número del 1 al 10."""
    
def aprender_tablas(numero):
    for num in range(1,11):
        print(numero, "x", num, "=", (num * numero))

numero = int(input("Ingrese un numero para aprender su tabla: "))
aprender_tablas(numero)