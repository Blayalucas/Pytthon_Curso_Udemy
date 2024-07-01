# thread com while com is_live

"""
Podemos também fazer um thead com while 

"""


# chamando a biblioteca sleep  e Thread
from time import sleep
from threading import Thread

# Def
def movimento  (texto,tempo):
    sleep(tempo)
    print(texto)
    
# instancia com temporizador 
    
t1 = Thread(target = movimento , args= ( "Pronto carregou", 2))
t1.start()

# Wrile 

while t1.is_alive():
    print("aguarde esta carregando")
    sleep(.3)
