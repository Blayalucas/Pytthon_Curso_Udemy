# Decorators - com Flask 

"""
Framework é um grande conjunto de bibliotecas
para criar uma funçao especifica
"""

"""
O flask  é um pequeno framework web escrito em Python.
Criado de site ( ele usa o Decorator para definir) o link para acessar
a pagina

Para iniciar o Flask você importa ele 

e cria uma "variavel" app  = FLASH (_NAME_)
e criar um DECORATOR @app.route("/home")  para definir o link para puxar
a função HOMEPAGE e demais DEF - sempre colocando DECORATOR @app.route("/home")
ou DECORATOR @app.route("/contatos")

e depois colocar ele para rodar  app.run()


Cada pagina que vai ter no site é uma função DEF
ou seja, quanto mais def mais paginas

quando rodar o codigo vai gerar um link copia o codigo e joga no 
google

OBS:Todos  decorator  atribui tudo que estiver embaixo dele. 

neste caso o decorator @app.route () "flask" ele informa qual link esse 
cara vai aparecer 

e quando chama a @login_required abaixo 
o usuario só irá acessar com apenas com o login

# O decorator uma vez criado facilita a vida
"""

from flask import Flask

app = Flask(__name__)

@app.route("/home")
def homepage():   # primeira pagina 
    return "Essa é minha HomePage"  # returna o que ele quiser 

@app.route("/contatos")
def contatos ():
    return "Esse são meus contatos"

app.run()