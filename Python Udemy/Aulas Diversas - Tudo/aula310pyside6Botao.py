# Pyside6 criando botão - QtWidgets 

"""
Widgets são os principais elementos que aparece na tela 

ex: um botão grafico 
    
"""
# Importando a biblioteca 
import sys


from PySide6.QtWidgets import QApplication, QPushButton

# Instancia de classes - QApplication com argumentos 
app = QApplication(sys.argv)

# Criacao de botão 
botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px;')



# Criacao de botão
botao2 = QPushButton('Botao2')
botao2.setStyleSheet('font-size: 40px;')

# O loop da aplicação
app.exec() 