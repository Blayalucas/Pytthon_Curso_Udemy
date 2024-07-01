# Modulo Random Choise     

"""
O Choise é um Sample um pouco melhorado ele é util para fazer um sorteio.
retornando apenas valores dentro da lista

"""

import random

r_shuffle = ["Lucas","Gilson","Rosa","Katia","Kahena"]
r_choise = random.choices(r_shuffle, k=2)
print(r_choise)