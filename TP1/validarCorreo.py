# Email (nombre@dominio.com) (el nombre debe comenzar con letra y puede tener números, guion_bajo, puntos y guion-medio)
# (definir 5 dominios y 5 países) DOMINIOS: .com, .net, .edu, .org, .mil    PAISES: .ar(argentina), .br(brasil), .ca(canada), .co(colombia), .cl(chile)
# ARCHIVO3.TXT

import re

regex = '^[a-z]([a-z|0-9|-|_])+@(gmail|hotmail)\.(com|net|edu|org|mil)\.(ar|br|ca|co|cl)'   #que empiece con una letra de la [a-z]
                                                                                            #que siga con una letra [a-z o un numero 0-9 ó - ó _] un numero, o una letra lo que sea una o mas veces
                                                                                            #@ (ó gmail ó hotmail) escapo el punto con la barra \. (com|net|...|mil . ar|br|...|cl

#regex = '^[a-zA-Z]([a-zA-Z]|[0-9]|[-]|[_])+@(gmail|hotmail)\.(com|net|edu|org|mil)[\.(ar|br|ca|co|cl)]?$'
#regex = '[a-zA-z0-9._-]+@[\w]+\.[net|com|biz]{3,}(\.[nl|us|uy|ca|ar]{2,})?$'   #DE PABLO
f = open("./archivo3.txt", "r")
#cadena = f.readline()  #no hace falta lo interpreta solo
for cadena in f:
    print(cadena)
    ip = re.compile(regex)
    if ip.match(cadena):
        print(">>Correo electronico valido!\n")
    else:
        print(">>>>Correo electronico INVALIDO\n")

f.close()