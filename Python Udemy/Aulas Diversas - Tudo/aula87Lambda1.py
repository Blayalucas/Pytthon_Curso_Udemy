# Função Lambda em Python 

"""
É uma função igual qualquer outra, porém são funções anonimas 
que contem apenas uma linha, ou seja, 
tudo deve ser contido de uma unica expressão. 

Ela "substitui" o Def 

"""
# Exemplo Def

def somaQuadrados (a,b):
    somaQ = a**2 + b**2
    return somaQ



somaQuadrados(2,3)

# exemplo lambda  -  

#Formula : Variavel = lambda faz o parametro : formula  

# lambda é uma "variavel" dentro da variavel

somaQuadrados = lambda a,b : a**2 + b**2 # a,b "parametro" e a**2 +b**2 " formula"
print(somaQuadrados (2,3))

