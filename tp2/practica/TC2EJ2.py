from automata.fa.nfa import NFA

nfa = NFA(
    states={'Estado1', 'Estado2', 'Estado3', 'Estado4', 'Estado5'},
    input_symbols={'a', 'b'},
    transitions={
        'Estado1': {'a': {'Estado2'}, 'b': {'Estado3'}, '': {'Estado3'}},
        'Estado2': {'a': {'Estado3'}},
        'Estado3': {'a': {'Estado5'}, '': {'Estado1'}, 'b': {'Estado4'}, '': {'Estado5'}},
        'Estado4': {'b': {'Estado5'}},
        'Estado5': {'': {'Estado3'}}
    },
    initial_state='Estado1',
    final_states={'Estado5'}
)

val = input("Ingrese la cadena: ")

if nfa.accepts_input(val):
    print('Aceptada')
    asd = nfa.read_input_stepwise(val)
    for f in asd:
        print(f)
else:
    print('Rechazada')