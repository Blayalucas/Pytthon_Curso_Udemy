# Classe Abstrata no Python são chamadas ABC

"""
Para importar ela fazemos 
"""

from abc import ABC


class log( ABC):  # Classe abstração herda da biblioteca ABC
    def log (self, msg): 
        raise NotImplementedError (" Implemente o metodo log ")
    
    def log_error(self,msg): # Metodo concreto (faz algo? tipo erro  ) aqui foi criado um error 
        return self.log(f'Error: {msg}')
    
        
    def log_sucess(self,msg): # metodos cocretos, ou seja que fazem coisa 
        return self.log(f'Sucess: {msg}')
    
# OU 

from abc import ABCMeta


class log(metaclass = ABCMeta):  # ou dessa forma 
    def log (self, msg): 
        raise NotImplementedError (" Implemente o metodo log ")
    
    def log_error(self,msg):  
        return self.log(f'Error: {msg}')
    
        
    def log_sucess(self,msg):  
        return self.log(f'Sucess: {msg}')
    