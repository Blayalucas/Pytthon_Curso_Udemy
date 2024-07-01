# Encapsulamento (public, protected, private )

"""
public = sem underline 

protected = uma underline _underline 

private = duas underline __underline

"""

class FOO:
    def __init__(self):
        self.public = "Isso é publico"  # sem underline 
        
    
    def metodo_publico(self):
        return " metodo_publico"
    
    
f = FOO ()
print(f.public)

print(f.metodo_publico())

