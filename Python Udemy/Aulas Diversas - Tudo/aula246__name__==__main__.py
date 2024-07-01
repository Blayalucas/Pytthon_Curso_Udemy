# if __name__ == __main__

"""
Para executar com perfeição o if __name__ == __main__
é necessario criar 2 arquivo um nome aleatorio e um 
outro também com nome aleatorio.

Exemplo: 

aula247app.py

aula248modulo.py 


No arquivo 248 teremos:

def soma (x : float , y: float ):
    return x + y 
    

if __name__ == __main__
    print(soma(10,20))
    print(soma(20,40))
    

No arquivo 247 teremos: 

from modulo import soma
print(soma(10,20))
print(soma(20,40))
    

OBS: Os arquivos se comunicam faz uma junção 

"""

