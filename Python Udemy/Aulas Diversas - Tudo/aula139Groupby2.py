# GROUPBY - 

from itertools import groupby

alunos = [
{'nome': 'Luiz','nota':'A'},
{'nome': 'Leticia','nota':'B'},
{'nome': 'Fabricio','nota':'A'},
{'nome': 'Rosemary','nota':'C'},
{'nome': 'Joana','nota':'D'},
{'nome': 'João','nota':'A'},
{'nome': 'Eduardo','nota':'B'},
{'nome': 'André','nota':'A'},
{'nome': 'Anderson','nota':'C'},

]

def ordena(alunos):  # Funcao ordena para ordernar os alunos 
    return alunos['nota']


alunos_agrupados = sorted(alunos,key = ordena) # colocando os alunos em ordem de NOTA
grupos = groupby(alunos_agrupados,key = ordena) # agrupando os alunos agrupados

for chaves, grupo in grupos:  # fazendo um for com biblioteca {}
    print(chaves)
    for alunos in grupo: # dentro dessas {} cada objetos separadinho
        print(alunos)