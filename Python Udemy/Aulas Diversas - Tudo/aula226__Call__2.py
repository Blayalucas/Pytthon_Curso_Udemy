# Methodo Call 

"""
Callable em classes normais , __call__ faz a instancia de uma classe ser executada 
"Foco  é a Intancia"


"""

class CallMe:
    def __init__(self, phone):
        self.phone = phone
        
    def __call__(self, nome):
        print(nome, "Chamando",self.phone)
        
    
call = CallMe("986543877")
call ("Lucas Blaya ") 

# Sempre faz class, Def Call, instancia e chama instancia com ()