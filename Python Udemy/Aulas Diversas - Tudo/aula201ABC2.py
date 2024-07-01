# Classe Abstrata ABC 

from abc import ABC  # Mãe 


class log( ABC): # "Filha" herda da biblioteca " Mãe "
    def log (self, msg): 
        raise NotImplementedError (" Implemente o metodo log ")
    
    def log_error(self,msg):  # Neta 
        return self.log(f'Error: {msg}')
    
        
    def log_sucess(self,msg): # Bisneta 
        return self.log(f'Sucess: {msg}')
    


class LogPrintMixin(log): # Subclasse
    def log(self, msg):
        print(f'{msg} {self.__class__.__name__}')
        

l = LogPrintMixin()
l.log_error ("oi")