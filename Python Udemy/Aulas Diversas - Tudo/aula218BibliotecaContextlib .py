#  Biblioteca Contexlib com ContextManager - Para Abrir um arquivo 

from contextlib import contextmanager

# Para abrir um arquivo SEMPRE fazer essa boa pratica, igual um init 

@contextmanager
def my_open(caminho_arquivo, modo): 
        print("Abrindo arquivo")
        arquivo = open (caminho_arquivo, modo, encoding= "UTF8")
        yield arquivo
        

with my_open ("aula 218.txt", "w") as arquivo:
        arquivo.write("Linha 1\n")
        arquivo.write("Linha 2\n")
        arquivo.write("Linha 3\n")
        print("With", arquivo)