# Signal  


"""

É uma segunda ação que criamos no site com Def 
    
"""

# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> signal ( segunda ação)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys

from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton, QWidget)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita')

botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

grid_layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# Função de slot da primeira acão 
def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')
    
# Função de slot da segunda ação.

def outro_slot(checked):
    print("Está marcado?", checked)


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar com primeira ação 
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(  # type:ignore
    lambda: slot_example(status_bar)
) 

# Signal - Segunda ação que criamos com junção da primeira e deixa a segunda com um Check : ✔
segunda_acao = primeiro_menu.addAction('Segunda ação')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect (outro_slot)

window.show()
app.exec()  # O loop da aplicação