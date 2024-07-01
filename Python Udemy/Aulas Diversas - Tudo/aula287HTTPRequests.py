# HTTP Requests

"""
Requests é uma biblioteca HTTP 

A mensagem de requisição do cliente deve incluir dados como:
- O método HTTP
- leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
    
- escrita - POST, PUT (substitui), PATCH (atualiza), DELETE
- O endereço do recurso a ser acessado (/users/)
- Os cabeçalhos HTTP (Content-Type, Authorization)
- O Corpo da mensagem (caso necessário, de acordo com o método HTTP)

"""

import requests

# 1 Passo: Criar uma URL 
url = 'https://www.youtube.com/'

# 2 Passo: Criar uma get leitura 
response = requests.get(url)

#3 Passo ; Verificaçao 
print(response)  #Response [200]> - Sucesso 



