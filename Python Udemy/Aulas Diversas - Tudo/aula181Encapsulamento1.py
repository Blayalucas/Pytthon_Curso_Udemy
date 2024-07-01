# Encapsulamento  (esconder)

"""
Encapsulamento (esconder) é um dos pilares da programação orientada a objetos, 
segundo o qual procuramos esconder de clientes (usuários de uma classe) 
todas as informação que não são necessárias ao uso da classe.

Por exemplo, suponha que precisássemos criar uma classe para
armazenar informações de funcionários de uma empresa, 
como ilustrado no exemplo abaixo.

então usamos (dois _underlines) não deveriam ser acessados fora da classe

# __horas_trabalhadas = 0 

"""
class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0 
        self.__salario = 0 

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada





