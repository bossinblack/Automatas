#Que contenga una letra mayúscula.Que contenga una letra minúscula.Que contengan al menos un número.Que contenga al menos un símbolo (definir 5 símbolos).Longitud mínima de 8 caracteres.
#ARCHIVO1.TXT

import re
simbolos = '[@, #, $, %]+'
numeros = '[0-9]+'
min = '[a-z]+'
may = '[A-Z]+'

f = open("./archivo1.txt","r")#abro el archivo

#cadena = f.readline()   #no hace falta lo interpreta solo
for cadena in f:
    print(cadena)
    size = len(cadena)  #cuento la cantidad de caracteres
    if re.search(simbolos, cadena) and re.search(numeros, cadena) and re.search(min, cadena) and re.search(may, cadena) and (size >= 8):
        print(">Contraseña Segura!\n")
    else:
        print(">>>Contraseña Insegura! No cumple con al menos uno de los requisitos\n")

f.close()