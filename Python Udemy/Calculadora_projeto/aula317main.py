# Projeto Calculadora 

"""
Esse é um projeto para criar uma calculadora virtual - Abrindo Janelas (padrão)

Passo a Passo : 

# Passo 1 : criar uma __main__

"""
# 2 Passo - Criar Janelas

# Biblioteca 

import sys
from Pyside6.Qtwidgets import (QApplication, QmainWindow, Qwidget, QvBoxLayout, QLabel)

# importanto para a aula 319
from aula319main_widow_class import Mainwindow

# Inicio da Main e abrindo o aplicativo 
if__name__ == '__main__'
    app = QApplication (sys.argv)
    
# Abrindo as janelas ( Padrão)
    window = Mainwindow()
    central_widgets = Qwidget()
    layout_vertical =  QvBoxLayout()
    central_widgets.setLayout(layout_vertical)
    
# Label ou rotulo texto

    label1 = QLabel(" Meu texto aqui")
    layout_vertical.addwidget(label1)
    
    window.setCentralWidget(central_widgets)
    window.adjustFixedSize()
    
    window.show()
    
    
# Executando o Aplicativo
    app.exec()