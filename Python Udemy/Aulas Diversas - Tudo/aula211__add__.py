# Dunder - __ADD__


class Ponto: 
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
        
    def __repr__(self):    
        class_name = type(self).__name__
        return f'{class_name}(x={self.x}, y={self.y})'
    
    def __add__(self,other):
        return "Bola"
        
        

p1 = Ponto(1,2)
p2 = Ponto(978,876)
p3 = p1 +p2


print(p1)
print(p2)
print(p3)

