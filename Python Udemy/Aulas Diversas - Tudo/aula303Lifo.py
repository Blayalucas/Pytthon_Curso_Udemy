# Deque - trabalhando com Lifo "pilha" - list do python 

"""
LIFO ( last in First Out)
Pilha ( stack)
É colocar os arquivos em pilha " um encima do outro"

Exemplo: Coloco em uma mesa um livro, dois livros, três livros 
um encima da outro 

na hora de tirar vou tirar ao contrario : três, dois, um 

1, 2,3
3,2,1

OBS: Boa pratica: 

APPEND:  para incluir 

POP:  para remover

"""
# biblioteca deque 

from collections import deque

# instancia em lista 
lista = [0,1,2,3,4,5,6,7,8,9]

# Add item na lista 
lista.append(10)
lista.append(11)

# instancia de remover item 
primeiro_removido = lista.pop()

# print para mostrar o ultimo e o que foi removido
print("ultimo:", primeiro_removido)
print("lista", lista)

