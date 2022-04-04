import re

cadena = input("Ingrese una cadena para analizar: ")
patron = '[A-Z]'
print(re.match(patron, cadena))