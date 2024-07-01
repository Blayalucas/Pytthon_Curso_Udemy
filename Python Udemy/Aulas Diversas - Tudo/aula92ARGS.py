# ARGS e KWARGS - Como utilizar? Python

"""
O Args aparece dentro de uma função DEF é uma tucla que vai receber 
todos os valores passados depois do primeiro valor
OBS: ao inves de criar varios parametros cria 2 no maximo usando o args

OBS: Args suga todas as informações que passar para ele 

def soma (a, b,*args)
soma (1,2 "Qualquer "Coisa")  o args sera ("Qualquer "Coisa") o a e b 1 e 2

No parametro sempre colocar os VALORES iniciais depois os *args

def calcular_imposto(valor,*args):  ou 
def calcular_imposto(valor,*imposto): ou 
def pessoas (valor,*dados_pessoais): # coloca tudo dentro de dados
                                    no final declara no print...

"""
"""
# exemplo sem args

def calcular_imposto(valor,perc_ir):  # sem args
    ir = valor * 0.275                 
    iss = valor * 0.05              
    csll = valor *0.0375
    pis = valor * 0.03
    return ir + iss + csll + pis
print(calcular_imposto(1000, perc_ir=0.275,)) # valor do parametro


"""
# exemplo com * args

def calcular_imposto(valor,*args):  # O valor primeiro, depois *args com tudo dentro
   total_imposto = 0  # contador apartir do 0
   for item in args: # sacola o que tem dentro do args
       total_imposto += valor * item  # total_imposto irá receber somar o valor * item
   return total_imposto

print(calcular_imposto (1000,0.275,0.05,0.0375,0.03 )) # valor do parametro