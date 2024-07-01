# Signal


"""

É uma terceira ação que criamos no site com Def 
    
"""

# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> signal ( segunda ação)
#               -> signal(terceiro slot)
#                   -> Layout (layout)
#                        -> Widget 1 (botao1)
#                           -> Widget 2 (botao2)
#                               -> Widget 3 (botao3)
#                   -> show
#               -> exec
import sys

from PySide6.QtWidgets import (
    QApplication, QGridLayout, QMainWindow, QPushButton, QWidget)


# Aplicações do site 
app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha janela bonita')

# criações de botões 
botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

# central Widget 
grid_layout = QGridLayout()
central_widget.setLayout(layout)

# Layout e ordem dos botões 

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# Função de slot da primeira acão


def first_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')

# Função de slot da segunda ação.


def second_slot(checked):
    print("Está marcado?", checked)

# Função de slot da terceira ação para receber uma actioon qualquer foi checada


def third_slot(action):
    def inner():
        second_slot(action.isChecked())
    return inner


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar com primeira ação
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(  # type:ignore
    lambda: first_example(status_bar)
)

# Signal - Segunda ação que criamos com junção da primeira e deixa a segunda com um Check : ✔
segunda_acao = primeiro_menu.addAction('Segunda ação')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(second_slot)
segunda_acao.hovered.connect(third_slot(segunda_acao))

window.show()
app.exec()  # O loop da aplicação
