# Try e o Except: 

"""
O try você cria o bloco de comando (estrutura)


resumindo : falo Try tenta fazer isso para mim  se der merda aparece o 

except:
    print( algum texto XXXXxxXXX)

ou seja falo faz esse comando se tiver errado vem o except.

se o usuario digitar Oi pagapaio periquito 
vai aparecer o except

"""
# exemplo try le para mim
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
    print(f"O resultado é {r}")
# se tiver errado escreve na tela XXXXX
except: 
    print("Infelizmente um problema")