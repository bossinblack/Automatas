#Escriba un programa en Python que lea una cadena de caracteres por consola, e indique si la misma es válida según las siguientes condiciones:
#-Si la cadena comienza con un número, debe tener al menos una aparición del símbolo “7”
#-Si la cadena comienza con una letra, debe tener al menos una aparición de la letra “p” (mayúscula o minúscula)
import re
cadena = input("Ingrese una cadena para analizar: ")
patronN = '[0-9]'

x1 = re.match(patronN, cadena)
if(x1):
    print("La  cadena ingresada empieza con un NUMERO")
    x2 = re.search('7', cadena)
    if(x2):
        print("La  cadena ingresada tiene al menos un '7'\n")
        print("***CADENA VALIDA!***\n")
    else:
        print("La  cadena ingresada NO tiene ningun '7'\n")
else:
    print("La cadena ingresada empieza con una LETRA")
    x2 = re.search("(p|P)", cadena)
    if(x2):
        print("La cadena ingresada contiene al menos una vez la letra 'p' o 'P'")
        print("***CADENA VALIDA!***\n")
    else:
        print("La cadena ingresada NO contiene NINGUNA 'p' o 'P'")