# Functions
""""
Uma função é um bloco de código que só é executado quando é chamado.

Você pode passar dados, conhecidos como parâmetros, para uma função.

Uma função pode retornar dados como resultado.

def nome_da_funcao (): # Na Função você pode dar qualquer nome 
# dentro do parente você coloca  o que a função ira fazer 

OBS: Para deixar todos os objetos padronizados utiliza o upper 
os dados ficara em letras maiusculas

No def você não utiliza print e sim o return 

"""

produtos = ["ABC123", "abc012","ABS111","AbB222"]

texto = "abc012"


def tratar_texto(texto):
    texto = texto.upper()  # coloca todas as letras em maisculas
    texto = texto.strip() # ele tira tosos os espaços antes e depois do texto
    return texto    # return faz o papel do print 

texto = tratar_texto(texto)
print(texto)





