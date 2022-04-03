"""Escriba un programa en Python que lea una cadena de caracteres por consola, e indique si la misma representa un
comentario válido en Python."""

import re
cadena = input("Ingrese una cadena para analizar: ")
patronA = '#'
patronB = '"""[\s\S]*?"""'
patronC = '\'\'\'[\s\S]*?\'\'\''

if re.match(patronA, cadena) or re.match(patronB, cadena) or re.match(patronC, cadena):
    print("Comentario Valido para Python!")
else:
    print("NO es un comentario valido para Python.")