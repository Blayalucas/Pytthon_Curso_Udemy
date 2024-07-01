# Set - Conjuntos em Python (tipo Set)
# Conjuntos são ensinados na matemática 
# Set em python são alterados 

"""
Method	Description
add()	Adicionar 
clear()	Remover 
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others

"""
# exemplo
s1 = set("Lucas") # {'u', 'a', 'L', 's', 'c'} ou seja parece dicionario mas não é 
print(s1)





# Sets são eficientes para remover valores duplicados
# de Iteraveis

# - eles não tem indexes " indices"
# - eles não tem garantem ordem;

"""
Eles são iteráveis (for, in, not, in) ou seja, 
pode fazer um programa iteração - manipulação
"""