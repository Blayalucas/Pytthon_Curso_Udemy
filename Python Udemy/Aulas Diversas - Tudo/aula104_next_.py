# Iterators

"""
No Python (e, na verdade, em diversas outras linguagens), 
temos o conceito de iterador. Um iterador é sempre um iterável, 
mas que produz um valor a cada vez que é usado como 
argumento da função nativa next().

Um iterador deve sempre implementar o método next(),
no Python 2, ou __next__(), no Python 3.
Esse método deve retornar a exceção StopIteration 
quando não há mais valores para o iterador produzir.

OBS: Para fazer o next precisa fazer o iter

"""
lista = [0,1,2,3,4,5]
lista = iter(lista)
"""
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

"""


print(hasattr(lista, '_next_'))  # se fazer assim 