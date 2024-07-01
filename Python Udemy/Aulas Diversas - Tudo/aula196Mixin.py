# Mixin 

"""
Mixins são basicamente trechos de códigos que você 
vai precisar usar em diversas classes, sem ter que implementar
individualmente funcionalidades que podem facilmente
serem reutilizadas através do conceite de mixins 

"""

# Abstração 

class log: 
    def log (self, msg): 
        raise NotImplementedError (" Implemente o metodo log ")
    
    def log_error(self,msg):
        return self.log(f'Error: {msg}')
    
        
    def log_sucess(self,msg):
        return self.log(f'Sucess: {msg}')

class LogFileMixin(log): 
    def log(self, msg):
        print(msg)
        



class LogPrintMixin(log): 
    def log(self, msg):
        print(f'{msg} {self.__class__.__name__}')
        
        

if __name__ == '__Main__':
    l = LogFileMixin()
    l.log_error( "Qualquer Coisa")
    l.log_sucess("Legal deu sucesso")