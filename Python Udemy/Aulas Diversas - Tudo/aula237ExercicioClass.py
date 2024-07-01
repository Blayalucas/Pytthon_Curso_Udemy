# Exercicio

"""
Exercicio de Abstração com Herança, Encapsulamento e Poliformismo

Criando uma conta Bancária
    
"""

import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta,saldo= 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    
    
    @abc.abstractmethod
    def sacar(self, valor): 
        ...
    
    
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f"(Depositado{valor})")
        
        
    def detalhes(self, msg ):
        print(f"Seu saldo atual é {self.saldo:2f}{msg}")
    
    
    
class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor 
        
        
        if valor_pos_saque >= 0:
            self.saldo -= valor 
            self.detalhes(f"(Saque {valor})")
            return self.saldo
        
        
        print("Não foi possivel sacar o valor desejado")
        self.detalhes(f"(Saque Negado  {valor})")
        

class ContaCorrente (Conta):
    def __init__(self, agencia, conta,saldo= 0, limite= 0):
        super().__init__(agencia, conta,saldo)
        self.limite = limite
    
    
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor 
        
        
        if valor_pos_saque >= 0:
            self.saldo -= valor 
            self.detalhes(f"(Saque {valor})")
            return self.saldo
        
        
        print("Não foi possivel sacar o valor desejado")
        self.detalhes(f"(Saque Negado  {valor})")





cp1 = ContaPoupanca(8599, 25257-9, 45)
cp1.sacar(50)
cp1.depositar(1)
print("##")
cc1 = ContaCorrente(8599, 25257-9, 100)
cc1.sacar(50)
cc1.depositar(1)