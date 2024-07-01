# Exceptions 

"""
As exceções são eventos especiais (geralmente erros) que ocorrem em tempo de execução. 
Quando um erro desses ocorre, o Python cria um objeto do tipo Exception

# è uma obrigatóriedade colocar ERROR para comunicar um erro em python e um RAISE

"""

class MeuError( Exception):
    ...
    
def levantar():
    raise MeuError ( " A um erro aqui ")
 
"""
Podemos tratar um erro e deixar ele passar fazendo um TRY, Except para criar dentro
do except uma variavel 
"""   


try:
    levantar()
except MeuError as error:  # criamos uma variavel dentro do except
    print(error)