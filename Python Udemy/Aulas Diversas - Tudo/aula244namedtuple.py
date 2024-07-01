# Collection Namedtuple

"""
namedtupla e um tipo de tupla dentro de um metodo " Lista "

"""

from collections import namedtuple

Carta = namedtuple("Carta",  ["valor", "naipe"])

as_espadas = Carta ("A", "espadas ")

print(as_espadas)
print(as_espadas.valor)
print(as_espadas.naipe)

for valor in as_espadas:
    print(as_espadas)