# Agregação 

"""
Agregação é fazer uma ligação de uma classe a outra Classe
estilo Power Bi, ligando uma na outra.


"""
#Passo 1
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None   # Passo 3 criar self ferramenta
        
    #Passo 4 - Criar um property
    @property
    def ferramenta(self):
        return self._ferramenta
    
    #Passo 5 - criar um setter da ferramenta 
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
    
    
#Passo 2       
class FerramentaDeEscrever:
    def __init__(self,nome):
        self.nome = nome
        
    
    def escrever(self):
        return f"{self.nome} está escrevendo"
    

# Passo 6 - Criar um variveis
escritor = Escritor ("Lucas")
caneta = FerramentaDeEscrever (" Caneta Bic")

# Passo 7 - Agora estou lincando os dois
escritor.ferramenta = caneta

# Passo 8 
print(caneta.escrever())
print(escritor.ferramenta.escrever())


