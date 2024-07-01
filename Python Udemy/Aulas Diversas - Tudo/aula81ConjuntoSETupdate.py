
# Update == atualizar 

list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = [10, 11, 12]
"""
Set1 vai receber a list 2 e a set 2 a list 1, 
ou seja, ajuntar (conjunto)
"""

set1 = set(list2)    # criei set
set2 = set(list1)

# Atualizando Set1 + Set2 == juntando (conjunto)
set1.update(set2)

# Print a atualização no set 
print(set1)

# Pedindo para ajuntar a list3 ao set 1  - List é um parametro
set1.update(list3)
print(set1)  #  {1, 2, 3, 5, 6, 7, 10, 11, 12}