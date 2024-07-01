# Metodo Especial Call ou Callablo 

"""
Methodo __call__ tem como objetivo realizar uma junção, entre as classes
e o Def "call", ou seja, chama as partes.

Callable é algo que pode ser executado com parenteses, quando ver um error callable 
tem que olhar como fazer para executa-lo

"""

#Classe aleatoria
class Example:
    def __init__(self):
        print("Instance Created")

# Definindo  __call__ metodo
    def __call__(self):
        print("Instance is called via special method")

# Creando a instancia da class
e = Example()

# __call__ realizando o metodo call
e()