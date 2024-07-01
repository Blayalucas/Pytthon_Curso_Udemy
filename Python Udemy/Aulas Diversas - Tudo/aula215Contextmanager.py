# Context Manager 
    
"""
Gerenciadores de contexto em Python garantem o gerenciamento adequado de recursos. 
Eles lidam automaticamente com a configuração e a limpeza de recursos, 
tornando seu código mais seguro e legível. 
Eles são particularmente úteis ao lidar com recursos 
como arquivos ou conexões de banco de dados.

Usa a Class MyContextManager:
Def __enter__ para entrar e __exit__ para sair


"""

class MyContextManager:
    def __enter__ (self):
        print("Enter ")
        return 1234
    
    def __exit__ (self, class_exception, exception_, traceback_ ):
        print("Exit")
        

instancia = MyContextManager()

with instancia as alguma_coisa:
        print("With", alguma_coisa)
        

# Obs: Quando printar vai Acessar a palavra Enter e após o  With no meio e por fim o Exit 
# ou seja inicio, meio, fim