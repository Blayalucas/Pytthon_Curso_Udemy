# recebendo  class Window 

from Pyside6.Qtwidgets import (QApplication, QMainWindow, Qwidget, QvBoxLayout, QLabel)

# class MainWindow

class Mainwindow(QMainWindow):
    def __init__(self, parent:Qwidget | None = None, *args, **kwargs) -> None: 
        super().__init__(parent,*args,**kwargs)
        
# Abrindo as janelas ( Padrão) com self
        
        self.central_widgets = Qwidget()
        self.layout_vertical =  QvBoxLayout()
        self.central_widgets.setLayout(self.layout_vertical)

# Label ou rotulo texto

        self.label1 = QLabel(" Meu texto aqui")
        self.addwidgetTovLayout(self.label1)
        self.setCentralWidget(self.central_widgets)
        self.setWindowTitle("Calculadora")

# Ajustando o tamanho e largura da Calculadora 
    def adjustSize (self):
        self.adjustSize()
        self.setFixedSize (self.width(),self.height())
        
        
     def addWidgetTovLayout(self, widget: Qwidget):
        self.layout_vertical.addWidget(Qwidget)   
# Executando o Aplicativo

        window = Mainwindow
        window.show()

        self.app.exec()