#Dirección IPv4 (000.000.000.000-255.255.255.255)
#ARCHIVO2.TXT

import re
regex = '^(?:(?:25[0-5]|2[0-4][0-9]|''[01]?[0-9][0-9]?)\.){3}''(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'   #EXPLICAR

f = open("./archivo2.txt","r")
for cadena in f:
    print(cadena)
    ip = re.compile(regex)
    if ip.search(cadena):
        print(">>Direccion valida!\n")
    else:
        print(">>>>Direccion Invalida\n")

f.close()