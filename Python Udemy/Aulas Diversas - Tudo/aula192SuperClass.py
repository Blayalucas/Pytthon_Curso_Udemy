# Super Classe 

"""
Super() é utilizado entre heranças de classes, ele nos proporciona 
extender/subscrever métodos de umasuper classe (classe pai) 
para uma sub classe (classe filha)

"""
# Passo 1 - Criar uma classe com argumento
class MinhaString(str):
    # Passo 3 - def upper com variavel interna Super e dentro classe pai 
    def upper(self):
        retorno = super(MinhaString,self).upper()
        #retornado a variavel interna 
        return retorno
    
    
    

# Passo 2 - Criar variavel da classe
string = MinhaString("Lucas")
print(string.upper())