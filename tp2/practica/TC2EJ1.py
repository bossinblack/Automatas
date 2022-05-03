# Describa los AFN que aceptan los siguientes lenguajes con el alfabeto {a,b}:   1). (a|b)*

import re
#regex = "^[a-bA-B]*$"
regex = "^[aAbB]*$"

cadena = input("Ingrese cadena: ")
print("------Estado inicial 0: cadena ingresada------", cadena)
isMatch = re.match(regex, cadena)
if not isMatch:
    print("Cadena invalida. ")
else:
    for i in list(cadena):
        print(">>Estado 1:")
        if i == 'a':
            print("Pasa a estado 2 con A")
        elif i == 'b':
            print("Pasa a estado 2 con B")