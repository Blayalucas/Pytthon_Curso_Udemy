# Tipagem -Dica Extra 

"""
Tipagem é descriminar cada coisa  informações as coisas:

Exemplo: 

class Conta(abc.ABC):
    def __init__(self, agencia: int , conta: int ,saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
"""


class Conta(abc.ABC):
    def __init__(self, agencia: int , conta: int ,saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo