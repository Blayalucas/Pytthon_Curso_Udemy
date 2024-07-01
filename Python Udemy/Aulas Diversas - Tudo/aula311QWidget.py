# Pyside  com class  QWidget e central_widget

"""
A classe QWidget é uma classe base de todos os objetos da interface do usuário  
"""

# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets


import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

# intancia que recebe a biblioteca e o argumento 
app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

# Widget central que é o unico que estara na janela com layout 
# Que será responsavel por receber varios Qtwidget

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

# Fazendo os botões um ao lado do outro
layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# Central widget entra na hierarquia e mostre sua janela
central_widget.show() 
# O loop da aplicação
app.exec()  