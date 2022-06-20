import re
regex = "^[aAbB]*$"

cadena = input("Ingrese cadena: ")
isMatch = re.match(regex, cadena)
if not isMatch:
    print("Cadena invalida. ")
else:
    print("------Estado inicial A: cadena ingresada------", cadena)
    for i in list(cadena):
        if i == 'a' or i == 'A' or i == 'b' or i == 'B':
            print("Con %s Pasa a estado B" % i)
