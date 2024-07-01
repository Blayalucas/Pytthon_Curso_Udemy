# Product - 

"""

"""
from itertools import combinations, permutations, product

def print_iter(interator):
    print(*list(interator))


pessoas = [
    'joão', 'Joana','Luiz','Leticia',

]
camisetas = [
    ['pretas', 'branca'],
    ['P','M','G'],
    ['Masculino', 'Feminino','Unissex'],
    ['Algodão','Poliester'],
]
# identificar o que combination 
print("O que é Combination") # identificar o que combination 
print_iter(combinations(pessoas,2)) 

# Chamando a combinations de pessoas em grupo de 2
print("Como fica Permutation")
print_iter(permutations(pessoas,2)) 

# Combinação "Cartesiana"  - Aleatória da Loja 
print("O que é Product")
print_iter(product(*camisetas))
