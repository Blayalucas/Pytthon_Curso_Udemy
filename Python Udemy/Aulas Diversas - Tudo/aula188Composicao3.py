# Composição 

""""
É combinação de objetos, quando instanciamos objetos de uma classe 
dentro de outra, quando usamos objetos de uma classe dentro 
de outros objetos.

"""

# Passo 1 - Criar classe Cliente com lista 
class Cliente:
    def __init__(self,nome):
        self.nome = nome
        self.enderecos = []
# Passo 2 - Criar um def receber os endereços do cliente
    
    def inserir_enderecos(self,rua, numero):
        self.enderecos.append(Endereco(rua, numero))  # Passo 4 colocar o a classe endereco dentro do Cliente
    
# Passo 3 - Criar Classe Endereço 
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
        
# Passo 5 - Variaveis 

cliente1 = Cliente ("Maria")
cliente1.inserir_enderecos("Avenida Brasil", 54)

print(cliente1.enderecos[0].rua)

del cliente1  # Composição == Ele vai apagar todo o processo do codigo 
# lá no passo 1, ou seja tudo " Pai"
            