# Herança
    
"""
Aprendendo a chamar atributo da Classe " Mãe" inserindo dois underlines

Desenho de Herança: 

#     A             ou seja, a Classe Mãe A passa para B e C 
#   /   \           o ideal é só fazer A ate C o de fica complicado
#  B --- C
#   \   /
#     D
"""
# Passo 1
class Pessoa:  # Super Class
    def __init__(self,nome, sobrenome) :
        self.nome = nome
        self.sobrenome = sobrenome
        
        # Passo 5 - criar um metodo 
    def falar_nome_class(self): # metodo 
        print(self.nome,self.sobrenome, self.__class__.__name__) # chamando atributo da classe Pessoa 2 andurlines de cada lado


# Sub Class - Passo 2 
class Cliente (Pessoa):   
    ...    


# Sub Class - Passo 3 
class Aluno (Pessoa): 
    ...


# Passo 4 - variaveis 
c1 = Cliente("Luiz", "Otavio")
c1.falar_nome_class() # passo 6 - variavel no metodo
a1 = Aluno("Maria" , " Helena")
a1.falar_nome_class() # passo 6 - variavel no metodo