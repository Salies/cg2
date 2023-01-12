from PySide6.QtWidgets import QMainWindow, QGroupBox, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Preenchimento de polígonos')
        self.resize(600, 300)
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
        self.centralLayout.addWidget(edgeFillWidget)
        