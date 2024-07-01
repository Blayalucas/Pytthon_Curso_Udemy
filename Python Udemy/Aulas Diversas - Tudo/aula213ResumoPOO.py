


# Herança com 3 Classes com Super()

"""
Nas minhas palavras HERANÇA é quando criamos uma nova Classe e 
informamos que a class "filha" esta para "Neta" e a "Bisneta" está
para "Filha", ou seja 3 classe se "ligando" entre si: 

"""
# Exemplo: 

# class Filha
class Contato:              
    def _init_(self, nome, sobrenome): # Atributos da Classe " Filha"
        self. nome = nome 
        self.sobrenome = sobrenome

    def _str_(self):
        return f"{self.nome} {self.sobrenome} {self.telefone} {self.email}"
    
        

# class "Neta" que recebe a classe "Filha"
class ContatoTelefonico (Contato): 
    def _init_(self, nome, sobrenome, telefone):
        super()._init_(nome, sobrenome)
        self.telefone = telefone

# Class "Bisneta"
class ContatoEmail(Contato): 
    def _init_(self, nome, sobrenome, email):
        super()._init_(nome, sobrenome)
        self.email = email 
        
# Instancia da Classe
c1 = ContatoTelefonico (nome = "Lucas", sobrenome = "Blaya", telefone = "999998587")
c2 = ContatoEmail(nome = "Leo ", sobrenome = "Grava", email= "LeoGrava@bol.com")

print(c1)
print(c2)

