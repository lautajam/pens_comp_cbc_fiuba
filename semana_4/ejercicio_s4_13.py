"""
Se tiene un ticket de supermercado que se puede representar como una lista de tuplas (producto,precio).
    a. Hacer una función que reciba la lista y calcule y devuelva el total que hay que pagar.
    b. Ahora se tienen dos tickets. Juntar ambos y volver a calcular el total.
"""

# A)
def total_pagar(ticket_1):
    total = 0
    for producto in ticket_1:
        total = total + producto[1]
    return total

ticket_1 = [
    ("Mayonesa", 120),
    ("Ricota", 80),
    ("Carne", 400),
    ("Especias", 190),
    ("Sarten", 500),
    ("Manteca", 34),
    ("Papel higienico", 90),
]

print("El total a pagar de Ticket_1 es:", total_pagar(ticket_1))

print("------------------------------")
# B)

ticket_2 = [
    ('Galletas', 412), 
    ('Detergente', 464), 
    ('Arroz', 198), 
    ('Leche', 328), 
    ('Jabon', 240), 
    ('Queso', 356), 
    ('Arroz', 338)
]

ticket_1.extend(ticket_2)

print("El total a pagar de Ticket_nuevo es:", total_pagar(ticket_1))