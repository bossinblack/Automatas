#URL (http-https://www……com) (puede o no figurar el protocolo, y el www) puede terminar con la /
#ARCHIVO4.TXT

import re
regex = '^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$'    #explicar

f = open("./archivo4.txt","r")
for cadena in f:
    print(cadena)
    ip = re.compile(regex)
    if ip.search(cadena):
        print(">>URL Valida!\n")
    else:
        print(">>>>URL Invalida\n")

f.close()