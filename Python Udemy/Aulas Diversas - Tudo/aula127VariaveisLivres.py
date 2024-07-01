# Variaveis Livres + NonLocal

""""
POdemos criar um Def com um DEF interno e pedi para 
return a variavel de fora internamente

Ou seja a variavel livre é o 

a de fora

"""

def fora ():
    a = 1

    def dentro():
        return a
    return dentro 