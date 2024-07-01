# Classes Abstrata 

"""
É um tipo de classe especial que não pode ser instanciada, apenas herdada. 
Sendo assim, uma classe abstrata não pode ter um objeto criado a partir de sua instanciação. 
Essas classes são muito importantes quando não queremos criar um objeto a partir 
de uma classe “geral”, apenas de suas “subclasses”.

Classes abstrata no Python são chamadas de ABC

São usada para criar novas classes ela podem força nova classes a criar metodos 



"""

class log:  # Classe abstração " força outras classes a criarem algo "
    def log (self, msg): 
        raise NotImplementedError (" Implemente o metodo log ")
    
    def log_error(self,msg): # Metodo concreto (faz algo? tipo erro  ) aqui foi criado um error 
        return self.log(f'Error: {msg}')
    
        
    def log_sucess(self,msg): # metodos cocretos, ou seja que fazem coisa 
        return self.log(f'Sucess: {msg}')
    
    