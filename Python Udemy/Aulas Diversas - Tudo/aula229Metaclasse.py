# Metaclasse em Python
"""
Uma metaclasse Python é como uma ferramenta mágica que permite personalizar o comportamento
de uma classe antes mesmo de ela ser criada. 
É como um tipo especial de classe usado para criar outras classes. 
Com uma metaclasse, você pode adicionar métodos ou atributos especiais 
a uma classe ou personalizar a maneira como uma classe é definida.


"""



class Pessoa: 
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia

    
    def __init__(self, nome):
        print('MEU INIT')
        self.nome = nome

p1 = Pessoa('Luiz')
