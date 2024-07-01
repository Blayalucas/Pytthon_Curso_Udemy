#  __repr__  Vs __Str__

"""
O __repr__ pega o objeto e converte para sua representação em string.
Ambos pegam o objeto e convertem para sua representação em string. 

"""

class Ponto: 
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        
    def __repr__(self):    
        class_name = type(self).__name__
        return f'{class_name}(x={self.x}, y={self.y})'

p1 = Ponto(1,2)
p2= Ponto(978,876)

print(p1)
print(p2)

