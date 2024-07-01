# Try / except com varios Erros

""""
Identificando erro para mim não se perder

ou seja erros basico que podem acontecer para cada ação

"""


try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
# se tiver um erro de X coisa vai 
except(ValueError, TypeError,IndexError):
    print("Tivemos um erro no tipo de informação digitada")
except(ZeroDivisionError):
    print("Não foi possivel dividir número com Zero")
except(KeyboardInterrupt):
    print("O usuario preferiu não informar dados ou senha")
else:
    print(" o resultado é {r:.2f}")
finally:
    print(" Volte sempre, muito obrigado")
