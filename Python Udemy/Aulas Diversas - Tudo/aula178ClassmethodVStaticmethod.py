# Exemplo de classmethod e staticmethod 

""""
Exemplo de como faz e quando usar classmethod ou  staticmethod 
"""
# criando a class Connection
class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None
    

    # Criando um login "User"
    def set_password(self,user):
        self.user = user
    
    # Criando um password "password"
    def set_password(self, password):
        self.password = password
        
    # criando Classmethod user e password e return 
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    