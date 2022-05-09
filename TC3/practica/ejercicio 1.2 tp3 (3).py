print("Ingrese su cadena:")
x=input()


#comienzo definiendo el estado a
def estadoA(x):
    if len(x) == 0:
        print("Cadena aceptable")

    else:
        print("Estado A, input:",x[0])
        if x[0] == 'a':
            estadoB(x[1:])
        elif x[0] == 'b':
            estadoC(x[1:])

#defino el estado b
#  
def estadoB(x):
    if len(x) == 0:
        print("Cadena aceptable")

    else:
        print("Estado B, input:",x[0])
        if x[0] == 'a':
            estadoB(x[1:])
        elif x[0] == 'b':
            estadoC(x[1:])

#Defino c
def estadoC(x):
    if len(x) == 0:
        print("Cadena aceptable")

    else:
        print("Estado C, input:",x[0])
        if x[0] == 'a':
            estadoB(x[1:])
        elif x[0] == 'b':
            estadoC(x[1:])
#defino D
def estadoD(x):
    if len(x) == 0:
        print("Cadena aceptable")

    else:
        print("Estado D, input:",x[0])
        if x[0] == 'a':
            estadoB(x[1:])
        elif x[0] == 'b':
            estadoC(x[1:])



estadoA(x)