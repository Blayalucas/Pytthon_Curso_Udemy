# Label ( Rotulo de texto)

import sys
from Pyside6.Qtwidgets import (QApplication, QmainWindow, Qwidget, QvBoxLayout, QLabel)

# Inicio da Main e abrindo o aplicativo 
if__name__ == '__main__'
    app = QApplication (sys.argv)
    
# Abrindo as janelas ( Padrão)
    window = QmainWindow()
    central_widgets = Qwidget()
    layout_vertical =  QvBoxLayout()
    central_widgets.setLayout(layout_vertical)
    
# Label ou rotulo texto

    label1 = QLabel(" Meu texto aqui")
    window.addWidgetTovLayout(label1)
    
    window.setCentralWidget(central_widgets)
    window.adjustFixedSize()
    
    window.show()
    
    
# Executando o Aplicativo
    app.exec()