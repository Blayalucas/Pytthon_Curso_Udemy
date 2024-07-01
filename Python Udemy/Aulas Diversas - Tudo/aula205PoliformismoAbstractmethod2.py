# Polimorfismo Abstractmethod 

from abc import ABC, abstractmethod

class Notificacao: 
    def __init__(self, mensagem ) -> None:
        self.mensagem = mensagem 
        
    @abstractmethod
    def enviar(self) -> bool:... # vai retornar Bool
    
class NotificacaoEmail (Notificacao):
    def enviar(self) -> bool:
        print("E-mail: Enviando :", self.mensagem )
        return True
        
        

class NotificacaoSMS (NotificacaoEmail):
    def enviar(self) -> bool:
        print("E-SMS: Enviando :", self.mensagem )
        return False

def notificar(notificacao:Notificacao):
    notificacao_enviada = notificacao.enviar()
    
    if notificacao_enviada:
        print("Notificação enviada ")

    else:
        print("Notificação NÂO enviada")
        

notificacao_email = NotificacaoEmail("testando E-mail")
notificar(notificacao_email)


notificacao_sms = NotificacaoSMS("testando SMS")
notificar(notificacao_sms)