# Context Manager 2 

class MyContextManager: 
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo 
        self._arquivo = None
        
    
    def __enter__(self):
        print("Abrindo Arquivo")
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding= "UTF8")
        return self._arquivo
        
        

    def __exit__ (self, class_exception, exception_, traceback_ ):
        print("Fechando Arquivo")
        self._arquivo
        

with MyContextManager("aula216.txt", "w") as arquivo :
        print("With", arquivo)