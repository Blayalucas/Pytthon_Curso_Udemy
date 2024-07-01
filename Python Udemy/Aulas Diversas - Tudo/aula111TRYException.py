# TRY com except (  tratando TODOS OS ERROS)

"""
O Try  tenta executar o codigo forçadamente ocorreu "erros" execução
gera um erro ai ele pula para o except daquele erro

Pulando de casa em casa 

Quando faz um 

except Exception:
    print(" Erro Desconhecido")

ele trata TODOS OS ERROS
"""
# Exemplos  except com " variavel "

try: 
    a = 18
    b = 0
    c = a /b
except SyntaxError:
    print(" Erro de Sintaxe")

except : 
    print(" Dividiu por Zero")

except Exception:
    print("Erro Desconhecido")

print("Continua")
