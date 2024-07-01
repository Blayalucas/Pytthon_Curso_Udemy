# theads com Def

"""
Temos uma outra maneira de fazer um theads 

"""

# chamando a biblioteca sleep  e Thread
from time import sleep
from threading import Thread

# Def
def dormir (texto,tempo):
    sleep(tempo)
    print(texto)
    
# instancia com temporizador 
    
t1 = Thread(target = dormir, args= ( " Vamos dormi povo ", 5))
t1.start()

    
t2 = Thread(target = dormir, args= ( "amanha levanto cedo ", 8))
t2.start()

t3 = Thread(target = dormir, args= ( "tenho treino", 3))
t3.start()

# for com temporizador de 15 e 5 milesimo de segundo 

for i in range(15):
    print(i)
    sleep(.5)