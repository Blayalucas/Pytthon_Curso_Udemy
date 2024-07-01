# Theads com Class 

"""

Você pode executar varios comandos "por fora" junto com principal
    
"""

# chamando a biblioteca sleep  e Thread
from time import sleep
from threading import Thread

#Class init com super ( para chamar a class mãe)

class MeuThread(Thread):
    def __init__(self,texto,tempo):
        self.texto= texto
        self.tempo= tempo
        
        super().__init__()
        
# def para percorrer  o self

    def run (self):
        sleep(self.sleep)
        print(self.texto)
        

# Instancias chamando as class para serem executadas ao mesmo tempo

t1 = MeuThread("thread 1", 5)
t1.start()


t2 = MeuThread("thread 2", 3)
t2.start()

t3 = MeuThread("thread 3", 7)
t3.start()

for i in range(20):
    print(i)
    sleep(2)