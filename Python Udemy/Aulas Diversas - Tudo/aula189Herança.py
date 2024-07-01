# Herança 

""""
A herança é um tipo de relacionamento entre classes
que significa que uma classe é outra. É uma propriedade dos 
objetos que permite a criação de uma hierarquia entre eles.


Exemplos : 

Classe principal (Pessoa)  # Super Class 
    Nome 
    Sobrenome
    Idade 
    Peso 

Classe Filha (Cliente)  # Sub Class
    Medico
    E-mail 
    Endereço

"""
class Pessoa:  # Super Class
    def __init__(self,nome, sobrenome) :
        self.nome = nome
        self.sobrenome = sobrenome
        
        
# Sub Class
class Cliente (Pessoa):  # Posso Pessoa dentro do clientecolocar a informação da classe pessoa aqui
    ...    


# Sub Class
class Aluno (Pessoa): # Aluno  dentro de pessoa 
    ...


    
c1 = Cliente("Luiz", "Otavio")
c1 = Aluno("Maria" , " Helena")