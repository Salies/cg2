from edge_fill import EdgeFill
from PySide6.QtWidgets import QMainWindow, QGroupBox, QWidget, QHBoxLayout, QGridLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap
from PIL import ImageQt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Preenchimento de polígonos')
        self.resize(600, 300)
        self.edgeFill = EdgeFill()
        self.centralLayout = QHBoxLayout()
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.centralLayout)
        self.setCentralWidget(self.centralWidget)
        self.buildFloodFillWidget()
        self.buildEdgeFillWidget()
    
    # Carregando os arquivos de imagens
    # no caso do edge fill, é necessário construir a imagem
    def loadImages(self):
        pass

    # Função para construir widget to floodfill
    def buildFloodFillWidget(self):
        floodFillWidget = QGroupBox('Flood fill')
        self.centralLayout.addWidget(floodFillWidget)

    def buildEdgeFillWidget(self):
        edgeFillWidget = QGroupBox('Inversão de cores')
        edgeFillLayout = QGridLayout()
        # label para image
        self.edgefill_imgLabel = QLabel()
        # carrega a imagem padrão
        im = self.edgeFill.get_img()
        # converte a imagem de pillow pra qt
        imQt = ImageQt.ImageQt(im)
        # converte a imagem de qt pra pixmap
        pixmap = QPixmap.fromImage(imQt)
        # seta a imagem no label
        self.edgefill_imgLabel.setPixmap(pixmap)
        edgeFillLayout.addWidget(self.edgefill_imgLabel, 0, 0, 1, 2)
        # label para o botão de floodfill
        edgeFillButton = QPushButton('Preencher')
        edgeFillButton.clicked.connect(self.edgefill_fill)
        edgeFillLayout.addWidget(edgeFillButton, 1, 0, 1, 1)
        edgeFillWidget.setLayout(edgeFillLayout)
        self.centralLayout.addWidget(edgeFillWidget)

    def edgefill_fill(self):
        self.edgeFill.fill()
        im = self.edgeFill.get_img()
        imQt = ImageQt.ImageQt(im)
        pixmap = QPixmap.fromImage(imQt)
        self.edgefill_imgLabel.setPixmap(pixmap)