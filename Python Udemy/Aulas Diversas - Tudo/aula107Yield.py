# Gerador ==  Yield

"""
Ele cria um generator, ou seja, 
cria uma lista de dados que vão sendo consumidos sob demanda. 
Em geral é usado para dar melhores abstrações ao código. 
Tudo que se faz com ele, dá para fazer sem ele de forma muito semelhante, 
mas expondo o mecanismo de geração dos dados.

Ele retorna um valor mantendo o estado de onde parou.
Quando executa de novo ele continua de onde parou. 

"""

def gera():
    variavel = "Valor 1"
    yield variavel  # chamando o gerador de variavel (loop)
    variavel = "Valor 2"
    yield variavel 
    variavel = "Valor 3"
    yield variavel 

gerador = gera()

for g in gerador:
    print(g)