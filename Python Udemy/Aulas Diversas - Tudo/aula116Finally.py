# Finally 

"""
O bloco finally SEMPRE executa após o término normal do bloco try 
mesmo que ocorra um erro.

"""
# imagine um arquivo e você quer fechar ele mesmo que ocorra um erro


try:
    print("Abrir arquivo")
    8/0  # erro de alguma coisa, tipo 8 não pode ser divido por 0
finally:
    print("Fechar arquivo")
