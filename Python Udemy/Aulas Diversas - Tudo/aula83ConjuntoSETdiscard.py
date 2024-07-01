
# Discard == descartar 

"""
Um def com parametro sets
dentro do SETS pedi para discard o numero 20
"""
def Remove(sets):
    sets.discard(20) # discard o 20 dentro do sets
    print (sets)
     
# Set aleatório 
sets = set([10, 20, 26, 41, 54, 20])
Remove(sets) # {41, 10, 54, 26} removeu todos os 20

