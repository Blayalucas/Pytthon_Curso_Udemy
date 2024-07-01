# Class decoradora 

"""
Class decoradora é o metodo da classe porém você. 
precisa faz uma função Def para chamar a classe decoradora 

class Multiplicar: 
    def __init__(self, func):  # init recebe um argumento 
        self.func = func 
        


@Multiplicar ( )   # isso 
def soma (x,y):
    return x + y
    
"""


# Passo 1 - Fazer uma classe
class Multiplicar: 
    def __init__(self, func):
        self.func = func
        

# Passo 2 - Chamar o Decorador 
@Multiplicar 
def soma (x,y):
    return x + y

# Chamar a Instancia 
resposta = soma ()
print(resposta)

# Continua na aula 228