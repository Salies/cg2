from PySide6.QtWidgets import QMainWindow, QPushButton, QGridLayout, QRadioButton, QWidget, QLabel
from PySide6.QtGui import QPixmap
from Objects import Objects
from PIL import ImageQt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Z-Buffer - Objetos")
        centralLayout = QGridLayout()
        centralWidget = QWidget(self)
        # Primeiro o label para exibir a imagem
        self.imgLabel = QLabel()
        # Já carregamos o label com uma imagem
        # Antes, carregamos os objetos
        self.objs = Objects()
        im = self.objs.to_img()
        # Transformando a imagem em uma imagem que o Qt pode exibir
        qim = ImageQt.ImageQt(im)
        self.imgLabel.setPixmap(QPixmap.fromImage(qim))
        centralLayout.addWidget(self.imgLabel, 0, 0, 1, 2)
        centralWidget.setLayout(centralLayout)
        self.setCentralWidget(centralWidget)
