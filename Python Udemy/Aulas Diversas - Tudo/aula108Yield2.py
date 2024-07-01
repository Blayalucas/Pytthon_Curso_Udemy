# Yield from

"""
Para realizar continuação do yield basta fazer uma 
yield from e continuar de onde parou 

"""

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1 ()
    yield 4
    yield 5
    yield 6

g = gen2()
for c in g:
    print(c)