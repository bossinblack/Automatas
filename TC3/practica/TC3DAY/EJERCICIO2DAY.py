import re

regex = "^[aaAA|bB]*(aA|bbBB)*$"

cadena = input("Ingrese cadena: ")
isMatch = re.match(regex, cadena)
if not isMatch:
    print("Cadena invalida. ")
else:
    print("------Estado inicial A: cadena ingresada------", cadena)
    state_a = 1
    state_b = state_c = state_d = state_e = 0
    for i in list(cadena):
        if state_a == 1:        #si estoy en el estado a
            if i == 'a' or i == 'A': #si entra una a
                print("Con %s Pasa a estado B" % i)
                state_b = 1
                state_c = state_d = state_e = state_a = 0
            elif i == 'b' or i == 'B': #si entra una b
                print("Con %s Pasa a estado C" % i)
                state_c = 1
                state_b = state_d = state_e = state_a = 0
        elif state_b == 1:      #si estoy en el estado b
            if i == 'a' or i == 'A': #si entra una a
                print("Con %s Pasa a estado D" % i)
                state_d = 1
                state_c = state_b = state_e = state_a = 0
            elif i == 'b' or i == 'B': #si entra una b
                print("Con %s Pasa a estado E" % i)
                state_e = 1
                state_d = state_c = state_b = state_a = 0
        elif state_c == 1:                       #si estoy en el estado c
            if i == 'a' or i == 'A': #y entra una a
                print("Con %s Pasa a estado B" % i)
                state_b = 1
                state_e = state_d = state_c = state_a = 0
            elif i == 'b' or i == 'B':#si entra una b
                print("Con %s Pasa a estado C" % i)
                state_c = 1
                state_b = state_e = state_d = state_a = 0
        elif state_d == 1:                      # si stoy en el estado d
            if i == 'a' or i == 'A':  # y entra una a
                print("Con %s Pasa a estado B" % i)
                state_b = 1
                state_c = state_d = state_e = state_a = 0
            elif i == 'b' or i == 'B':  # o si entra una b
                print("Con %s Pasa a estado C" % i)
                state_c = 1
                state_b = state_d = state_e = state_a = 0
        elif state_e == 1:                      #si stoy en el estado e
            if i == 'b' or i == 'B':  #y entra una b
                print("Con %s vuelve al estado D" % i)
                state_d = 1
                state_c = state_b = state_e = state_a = 0
            elif i == 'a' or i == 'A':  # y entra una a
                print("Con %s Vacio: queda en estado E" % i)
                break

