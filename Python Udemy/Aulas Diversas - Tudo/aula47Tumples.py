# Tuplas 

""""
Tuplas é uma variavel composta 
Podemos fazer com 3 tipos de ()[]{}

"""
#               0           1       2       3
lanches = ("Hamburguer", "Suco", "Pizza", "Pudin" )
print(lanches[:2]) # O python não le o ultimo elemento, aqui só hamburguer e suco ele para no 1
print(lanches[1:3]) # aqui ele le do suco ao pudin
print(lanches[-2]) # neste caso sera a pizza
print(lanches[-1])# neste caso sera a pudin
print(lanches[-3]) #neste caso sera o Suco
print(lanches [-3:]) # neste caso suco, pizza e pudin