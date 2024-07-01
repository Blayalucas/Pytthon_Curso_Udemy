# Classe exemplo top

"""
Exemplo muito bom para usar no dia a dia 

"""
class Camera: # camera é o self
    def __init__(self, nome, filmando= False):
        self.nome = nome
        self.filmando = filmando
        
        
# Filmando         
    def filmar(self):
        if self.filmando:
            print(f"{self.nome} já está filmando")
            return
        
        print(f"{self.nome} está filmando...")
        
# Pedindo para parar de Filmar 

    def parar_filmar(self):
        if not self.filmando:
            print(f"{self.nome} não está filmando...")
            return
        
        print(f"{self.nome} está parando de filmar...")
        self.filmando = False
        
# Fotografar
    def fotografar(self):
        if self.filmando:
            print(f"{self.nome} não pode fotografar filmando")
            return     
        
        print(f"{self.nome} está fotogrando ...")
        

c1 = Camera("Canon")
c2 = Camera ("Sony")
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

