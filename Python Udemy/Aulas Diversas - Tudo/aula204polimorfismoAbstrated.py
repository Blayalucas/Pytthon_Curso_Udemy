# Polimorfismo com abstractmethod

from abc import ABC, abstractmethod

class Notificacao: 
    def __init__(self, mensagem ) -> None:
        self.mensagem = mensagem 
        
    @abstractmethod
    def enviar(self) -> bool:...
    
class NotificacaoEmail (Notificacao):
    def enviar(self):
        print("E-mail: Enviando :", self.mensagem )
        
        

class NotificacaoSMS (NotificacaoEmail):
    def enviar(self):
        print("E-SMS: Enviando :", self.mensagem )
        

n = NotificacaoSMS("Mensagem por SMS Enviada ")
n.enviar()
        