# post_init_

"""
Na dataclass existem o post_init_ que é executado após o init 

Exemplo: def _post_init_(self):

"""

from dataclasses import dataclass

@dataclass
class Pessoa: 
    nome: str
    idade: int
    sobrenome: str
    nome_completo: str
    

    def _init_(self, nome, sobrenome, nome_completo):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.nome_completo = f"{self.nome} {self.sobrenome}"
        
    def _post_init_(self):
        print("Post Init ")
        

p1 = Pessoa("Lucas",36,"Blaya","Lucas Blaya")
print(p1)
print(p1._post_init_)