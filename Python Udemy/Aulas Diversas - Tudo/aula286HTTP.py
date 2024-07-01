# http 
"""
É um protocolo usado para enviar e receber dados na internet. 
Ele funciona no modo cliente/Servidor, onde o cliente 
( seu navegador ) faz uma requisição ao servidor.


A mensagem de requisição do cliente deve incluir dados como:
# - O método HTTP
#     - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
#     - escrita - POST, PUT (substitui), PATCH (atualiza), DELETE
# - O endereço do recurso a ser acessado (/users/)
# - Os cabeçalhos HTTP (Content-Type, Authorization)
# - O Corpo da mensagem (caso necessário, de acordo com o método HTTP)

"""

