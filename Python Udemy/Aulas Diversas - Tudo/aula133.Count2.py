# Count exemplo 2 com for e if 

"""
OBS: Lembrando que o count é infinito, se 
fazer um for precisa inserir um break 

""" 
from itertools import count  # Count é infinito

# Range é finito ele para

c1 = count(step=8, start=8) # Count começa contando de 8 em 8 - ex (8,16,24)
r1 = range(8,100,8) # Range não é iteraitor, ou seja, ele tem fim no caso 100


print('count')
for i in c1:
    if i > 100:
        break  # Break para parar no 100

    print(i)
print()
print('range')
for i in r1:
    if i > 100:
        break   # sempre é bom deixar um break de segurança

    print(i)
