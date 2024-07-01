# Metodo do Metodo - Metodo da Instancia

"""
Um carro tem "atributos" caracteristica (cor branca, marca) 
e tem comportamentos ações "metodos"(acelerar, freiar)

Passo a passo para criar uma classe perfeita 

Com atributos e metodos

"""

# Segundo Passo - Criar Atributos "Caracteristicas"
class Carro:
    def __init__(self, nome):
        self.nome = nome
        
        # Terceiro passo - Criar Metodo do Metodo "Ação"
    def acelerar (self):
        print(f"{self.nome} está acelerando") 


# Primeiro Passo 
fusca = Carro ("Fusca")

# Quarto passo - um unico print 
print(fusca.nome)
fusca.acelerar()