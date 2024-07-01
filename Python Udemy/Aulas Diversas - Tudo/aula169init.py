# Metodo Init 

"""

Ele é usado para inicializar o objeto quando 
vai criar uma instância daquela classe.

Ou seja, quando for fazer o primeiro DEF da classe usa o (init e o self) OBRIGATÓRIO

OBS: A Classe é um molde para fazer DEF

Conforme passo a passo 

"""
# Passo 2 
class Point:
    def __init__(self, x, y):  # _init_ e Self é obrigatorio
        self.x = x   # copia e cola os parametros e coloca = parametro
        self.y = y   # copia e cola os parametros e coloca = parametro

# Passo 1 
x = Point(1, 2)  # Variavel para receber os dados
print(x.x)