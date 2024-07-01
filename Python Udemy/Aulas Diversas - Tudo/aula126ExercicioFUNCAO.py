# Exercício - Adiando execução de funções - 


def soma(x, y):  # funcao Soma 
    return x + y


def multiplica(x, y):  # Funcao Multiplica 
    return x * y


def criar_funcao(funcao, x): # função para criar função dentro dela ou seja funcao dentro de funcao
    def interna(y):
        return funcao(x, y)    # funcao dentro de função
    return interna


soma_com_cinco = criar_funcao(soma, 5)  # variavel vai receber a funcao criar com soma 
multiplica_por_dez = criar_funcao(multiplica, 10) # variavel vai receber a funcao criar com multiplicacao 

print(soma_com_cinco(10))        # 15
print(multiplica_por_dez(10))    # 100