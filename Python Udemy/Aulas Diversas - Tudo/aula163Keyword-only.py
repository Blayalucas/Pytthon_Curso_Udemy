# Keyword - Only *

"""
Ele é diferente do *args - O Args suga tudo que foi informado e deixa em () dentro 
assim ("qualquer coisa") o *args fara isso. 

O keyword * informa no Def que posso acrescentrar uma LETRA VARIAVEL após as demais

Exemplo: 

def soma (a, b,*, c):   # aqui estou informando que terei um elemento a mais neste caso o C
colocando o c= 

"""

def soma (a, b,*, c):
    print(a + b + c)

soma(4, 5, c=7) # acrescentando c= +  o valor 