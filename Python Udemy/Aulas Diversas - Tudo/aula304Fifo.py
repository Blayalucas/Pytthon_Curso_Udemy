# Deque - trabalhando com FIFO " fila"

"""
FIFO é igual uma fila 

significa uma fila mesmo onde o primeiro a entrar 
é o primeiro a sair 

exemplo: 
Comprar um ingresso você é o primeiro a chegar, na 
frente de todos 

então você será o primeiro a ser atendido.  


obs: tempo linear
"""

# biblioteca deque 

from collections import deque

# instancia em lista 
lista = [0,1,2,3,4,5,6,7,8,9]

# inserindo um item  na lista como se fosse o primeiro da fila
lista.insert (10)
lista.insert (11)
# [11,10,0,1,2,3,4,5,6,7,8,9]


# instancia de remover item 
primeiro_removido = lista.pop()

# print para mostrar o ultimo e o que foi removido
print("ultimo:", primeiro_removido)
print("lista", lista)
#[10,0,1,2,3,4,5,6,7,8,9]


