import re
cadena = input("Ingrese una cadena para analizar: ")
patron = '[0-9]'
print(re.search(patron, cadena))