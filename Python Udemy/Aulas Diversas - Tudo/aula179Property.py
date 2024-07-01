#Property 

""""
Com o Property "Getter" você pode mudar o valor de uma classe
sem mudar o codigo inteiro

Imagine um programa enorme e você quer alterar apenas um pedaço 
então utilizamos o Property

"""

class Caneta:                   # passo 2
    def __init__(self, cor):
        self.cor_tinta = cor  # mudando o valor para chamar o property 
        
        
    # metodo property - Passo 4 
    """
    ele fez alteração no codigo" sem mudar nada do codigo
    """ 
    @property 
    def cor (self):# continua com a cor
        print("Property") # mostrando que aqui tem um property
        return "Qualquer coisa"
        
        
# Variavel recebendo a cor azul  - Passo 1 
caneta = Caneta("Azul")

# Se mandar printar a variavel azul - passo 3 

print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)