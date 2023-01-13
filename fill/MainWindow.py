from edge_fill import EdgeFill
from flood_fill import flood_fill, flood_fill_eight
from PySide6.QtWidgets import QMainWindow, QColorDialog, QRadioButton, QGroupBox, QWidget, QHBoxLayout, QGridLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap, QColor
from PIL import ImageQt, Image
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Preenchimento de polígonos')
        self.edgeFill = EdgeFill()
        self.centralLayout = QHBoxLayout()
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.centralLayout)
        self.setCentralWidget(self.centralWidget)
        self.buildFloodFillWidget()
        self.buildEdgeFillWidget()

    def floodfill_drawimage(self):
        imQt = ImageQt.ImageQt(self.floodfill_im)
        pixmap = QPixmap.fromImage(imQt)
        self.floodfill_imgLabel.setPixmap(pixmap)

    # Função para construir widget to floodfill
    def buildFloodFillWidget(self):
        floodFillWidget = QGroupBox('Flood fill')
        floodFillLayout = QGridLayout()
        # Primeira linha, duas colunas do grid com os radio buttons
        # "Vizinhança-4" e "Vizinhança-8"
        self.v4 = QRadioButton('Vizinhança-4')
        v8 = QRadioButton('Vizinhança-8')
        self.v4.setChecked(True)
        floodFillLayout.addWidget(self.v4, 0, 0)
        floodFillLayout.addWidget(v8, 0, 1)
        # Carregando imagem padrão
        self.floodfill_imgLabel = QLabel()
        self.floodfill_im_og = Image.open('img/Testar_FloodFill.bmp')
        self.floodfill_im = self.floodfill_im_og
        self.floodfill_drawimage()
        floodFillLayout.addWidget(self.floodfill_imgLabel, 1, 0, 1, 2)
        # Botão de mudar de cor e de redesenhar
        changeColorButton = QPushButton('Escolher cor')
        self.floodFillColor = (255, 0, 0)
        changeColorButton.clicked.connect(self.floodfill_change_color)
        floodFillLayout.addWidget(changeColorButton, 2, 0)
        floodfill_resetbutton = QPushButton('Reiniciar')
        floodfill_resetbutton.clicked.connect(self.floodfill_reset)
        floodFillLayout.addWidget(floodfill_resetbutton, 2, 1)
        # Evento para quando o usuário clicar na imagem do flood fill
        self.floodfill_imgLabel.mousePressEvent = self.floodfill_fill
        floodFillWidget.setLayout(floodFillLayout)
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
        edgeFillLayout.addWidget(edgeFillButton, 1, 0, 1, 2)        
        edgeFillWidget.setLayout(edgeFillLayout)
        self.centralLayout.addWidget(edgeFillWidget)

    def edgefill_fill(self):
        self.edgeFill.fill()
        im = self.edgeFill.get_img()
        imQt = ImageQt.ImageQt(im)
        pixmap = QPixmap.fromImage(imQt)
        self.edgefill_imgLabel.setPixmap(pixmap)

    def floodfill_change_color(self):
        colorDiag = QColorDialog()
        colorDiag.setCurrentColor(QColor(*self.floodFillColor))
        if colorDiag.exec():
            self.floodFillColor = colorDiag.currentColor().getRgb()[:3]

    def floodfill_fill(self, event):
        img_a = np.array(self.floodfill_im)
        x = event.pos().x()
        y = event.pos().y()
        color_at_pos = tuple(img_a[y, x])
        if self.v4.isChecked():
            flood_fill(img_a, y, x, self.floodFillColor, color_at_pos)
        else:
            flood_fill_eight(img_a, y, x, self.floodFillColor, color_at_pos)
        self.floodfill_im = Image.fromarray(img_a)
        self.floodfill_drawimage()

    def floodfill_reset(self):
        self.floodfill_im = self.floodfill_im_og
        self.floodfill_drawimage()