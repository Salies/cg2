from PySide6.QtWidgets import QMainWindow, QPushButton, QGridLayout, QHBoxLayout, QRadioButton, QWidget, QLabel, QSpinBox, QGroupBox
from PySide6.QtGui import QPixmap, QIcon
from Objects import Objects
from PIL import ImageQt
from numpy import radians

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Z-Buffer - Objetos")
        self.setWindowIcon(QIcon("ico/BTLPANEL.BIN_5.png"))
        centralLayout = QHBoxLayout()
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
        centralLayout.addWidget(self.imgLabel)
        # Criando um grupo para rotação
        rotGroup = QGroupBox("Rotação")
        rotLayout = QGridLayout()
        rotGroup.setLayout(rotLayout)
        # Os radiobuttons de rotação
        self.radioX = QRadioButton("X")
        self.radioX.setChecked(True)
        self.radioY = QRadioButton("Y")
        self.radioZ = QRadioButton("Z")
        rotLayout.addWidget(self.radioX, 0, 0)
        rotLayout.addWidget(self.radioY, 0, 1)
        rotLayout.addWidget(self.radioZ, 0, 2)
        # Na linha de baixo, os spinbox
        self.deg = QSpinBox()
        self.deg.setRange(-360, 360)
        self.deg.setValue(30)
        rotLayout.addWidget(self.deg, 1, 0, 1, 2)
        # Um label dizendo "graus"
        rotLayout.addWidget(QLabel("graus"), 1, 2)
        # E o botão de rotação
        self.rotButton = QPushButton("Rotacionar")
        self.rotButton.clicked.connect(self.rotate)
        rotLayout.addWidget(self.rotButton, 2, 0, 1, 3)
        # Stretch
        rotLayout.setRowStretch(3, 1)
        centralLayout.addWidget(rotGroup)
        centralWidget.setLayout(centralLayout)
        self.setCentralWidget(centralWidget)

    def rotate(self):
        # Pegando os graus
        deg = self.deg.value()
        deg = radians(deg)
        # Vê qual o eixo
        if self.radioX.isChecked():
            self.objs.rotate_x(deg)
        elif self.radioY.isChecked():
            self.objs.rotate_y(deg)
        elif self.radioZ.isChecked():
            self.objs.rotate_z(deg)
        # Agora atualiza a imagem
        im = self.objs.to_img()
        qim = ImageQt.ImageQt(im)
        self.imgLabel.setPixmap(QPixmap.fromImage(qim))
