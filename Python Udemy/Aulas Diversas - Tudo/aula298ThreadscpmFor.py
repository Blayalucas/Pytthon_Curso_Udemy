# Theads com for 


# chamando a biblioteca sleep  e Thread
from time import sleep
from threading import Thread

# fazendo uma Class init
class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        
# def para receber a classe com instruções
    def comprar(self, quantidade):
        if self.estoque < quantidade:
            print( " Não temos ingressos suficientes")
            return
        
        print(f"Você comprou {quantidade} ingressos."  
            f"Ainda temos {self.estoque}")
        self.estoque -= quantidade

# if para gerir o estoque com um for 
# necessario criar uma main.py a parte 

if __name__ =='__main__': 
    ingressos = Ingressos(10)
    
for i in range(1,10):
    t = Thread(target = ingressos.comprar, args= (i,))
    t.start()

