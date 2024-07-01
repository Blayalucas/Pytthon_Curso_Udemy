# Context Manager com exception em Classe 

"""
Quando Você faz um 
exception.add_note (" Minha Nota")
return True 

Você pode deixar o erro passar 

PORÉM NÂO é Boa Pratica 

"""


class MyContextManager: 
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo 
        self._arquivo = None
        
    
    def __enter__(self):
        print("Abrindo Arquivo")
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding= "UTF8")
        return self._arquivo
        
        

    def __exit__ (self, class_exception, exception_, traceback_):
        print("Fechando Arquivo")
        self._arquivo.close()
        exception_.add_note("Minha Nota")
        return True
        

with MyContextManager("aula217.txt", "w") as arquivo :
        arquivo.write("Linha 1\n")
        arquivo.write("Linha 2\n")
        arquivo.write("Linha 3\n")
        print("With", arquivo)