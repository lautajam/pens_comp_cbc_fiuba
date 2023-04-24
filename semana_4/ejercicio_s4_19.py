"""
Santiago armó una lista con el pedido de empanadas de su familia pero ahora quiere saber la cantidad
de gustos diferentes que tiene que pedir.
Hacer una función que según una lista de strings elimine todos los elementos repetidos y devuelva su
tamaño.
"""

gustos_empanadas = ['carne', 'pollo', 'jamón y queso', 
                    'humita', 'cebolla y queso', 'roquefort', 'caprese', 
                    'verdura', 'carne', 'pollo', 'choclo', 'jamón y queso', 
                    'pollo', 'jamón y queso', 'napolitana', 'jamón y queso', 
                    'pollo', 'choclo y queso', 'carne']

def cantidad(gustos_empanadas):
    for empanada in gustos_empanadas:
        cantidad = gustos_empanadas.count(empanada)
        if(cantidad > 1):
            gustos_empanadas.remove(empanada)
    return len(gustos_empanadas)

print("-------Antes de quitar repetidos-------")
print(len(gustos_empanadas))
print(gustos_empanadas)

print("-------Despues de quitar repetidos-------")

print(cantidad(gustos_empanadas))
print(gustos_empanadas)