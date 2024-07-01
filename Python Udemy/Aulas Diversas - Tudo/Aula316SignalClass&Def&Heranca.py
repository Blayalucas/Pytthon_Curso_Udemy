# Signal com Classe & DEf  & Herança

"""

A class MyWindow(QMainWindow) com a Função Def "obriga" colocar todo o site, 
dentro da Função Def com um self ( lembrando que é necessario retirar o Window na Central Windget)  
e colocar o self para dar bom o programa. 

Colocar todo o site dentro da Class 

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

from Pyside6.Qtcore import Slot # Biblioteca 
from PySide6.QtWidgets import (
    QApplication, QGridLayout, QMainWindow, QPushButton, QWidget)


# Aplicações do site 
app = QApplication(sys.argv)

# Criando Class QMainWindow com Def para inserir tudo dentro dela. 

class MyWindow(QMainWindow):
    def __init__(self, parent= None): 
        super().__init__(parent)

#Botão 1 - Dentro da Função Def
        self.botao1 = QPushButton('Texto do botão')
        self.botao1.setStyleSheet('font-size: 80px;')
        self.botao1.clicked.connect(self.second_slot)


        self.central_widget = QWidget()
        
# retire a palavra Window e coloque um self no lugar (será a propria janela) do site
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha janela bonita')
#Botão 2 - Dentro da Função Def
        self.botao2 = QPushButton('Botão 2')
        self.botao2.setStyleSheet('font-size: 40px;')
#Botão 3 - Dentro da Função Def
        self.botao3 = QPushButton('Botão 3')
        self.botao3.setStyleSheet('font-size: 40px;')

# Central Widget dentro tambem 
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

# Layout e ordem dos botões também 

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)
        

# statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

# menuBar com primeira ação

        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro menu')
        self.primeira_acao = self.primeiro_menu.addAction('Primeira ação')
        self.primeira_acao.triggered.connect(self.first_example)

# Signal - Segunda ação que criamos com junção da primeira e deixa a segunda com um Check : ✔

        self.segunda_acao = self.primeiro_menu.addAction('Segunda ação')
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.second_slot)
        self.segunda_acao.hovered.connect(self.second_slot)

# Função de slot da primeira acão

    @Slot()
    def first_example(self):
        self.status_bar.showMessage('O meu slot foi executado')

# Função de slot da segunda ação.

    @Slot
    def second_slot(self):
        print("Está marcado?",self. segunda_acao.isChecked())


window = MyWindow
window.show()
app.exec()  # O loop da aplicação