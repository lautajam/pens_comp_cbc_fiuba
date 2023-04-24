# Crear una secuencia con números distintos, y luego devolver el elemento máximo y el mínimo.

numeros_1 = [23,457,23,46,567,23523,458657,1]

numeros_2 = [534,658,3245,47,8709,4356,2346,6783]

numeros_1.sort()
numero_max = numeros_1[len(numeros_1) - 1]
numero_min = numeros_1[0]

print("El numero mayor de 'numeros_1[]' es:", numero_min)
print("El numero menor de 'numeros_1[]' es:", numero_max)

numeros_2.sort()
numero_max = numeros_2[len(numeros_2) - 1]
numero_min = numeros_2[0]

print("El numero mayor de 'numeros_2[]' es:", numero_min)
print("El numero menor de 'numeros_2[]' es:", numero_max)

