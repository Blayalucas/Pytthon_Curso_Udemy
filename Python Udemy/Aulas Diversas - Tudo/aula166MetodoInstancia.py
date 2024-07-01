# Metodo Instancia

"""

é necessário criar um objeto de sua classe. 
Vamos ver um exemplo de um método de instância.

Exemplo: 

Um carro tem "atributos" caracteristica (cor branca, marca) 
e tem comportamentos ações "metodos"(acelerar, freiar)

OBS: O Fusca dentro da class sempre sera Self fora da classe Fusca

# Observação _init_ e Self é obrigatorio dentro da DEF 

"""

# Segundo Passo 
class Carro:
    def __init__(self, nome):
        self.nome = nome


# Primeiro Passo 
fusca = Carro ("Fusca")

# Terceiro passo
print(fusca.nome)