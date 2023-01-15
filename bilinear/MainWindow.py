from PySide6.QtWidgets import QMainWindow, QGridLayout, QWidget, QLabel, QGroupBox, QRadioButton, QPushButton, QSpinBox
from PySide6.QtGui import QPixmap, QIcon
from bilinear import Ramp
from PIL import Image, ImageQt
from numpy import radians

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Superfícies bilineares")
        self.setWindowIcon(QIcon("ico/BTLPANEL.BIN_3.png"))
        # Criando o layout e widget principais
        layout = QGridLayout()
        widget = QWidget()
        widget.setLayout(layout)
        # Prepara a instância da rampa
        self.ramp = Ramp()
        # Retira uma imagem da rampa e coloca na label
        self.imgLabel = QLabel()
        self.imgLabel.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(self.ramp.to_img())))
        # Adiciona a label ao layout
        layout.addWidget(self.imgLabel, 0, 0)
        # À direita, adiciona o groupbox de rotação
        self.rotGroupBox = QGroupBox("Rotação")
        self.rotGroupBox.setLayout(QGridLayout())
        layout.addWidget(self.rotGroupBox, 0, 1)
        # Radiobuttons de eixo de rotação
        self.radioX = QRadioButton("X")
        self.radioY = QRadioButton("Y")
        self.radioZ = QRadioButton("Z")
        self.radioX.setChecked(True)
        self.rotGroupBox.layout().addWidget(self.radioX, 0, 0)
        self.rotGroupBox.layout().addWidget(self.radioY, 0, 1)
        self.rotGroupBox.layout().addWidget(self.radioZ, 0, 2)
        # Spinbox de graus
        self.degSpinBox = QSpinBox()
        self.degSpinBox.setRange(-360, 360)
        self.degSpinBox.setValue(30)
        # Label para graus
        degLabel = QLabel("graus")
        # Botão de rotação
        self.rotButton = QPushButton("Rotacionar")
        self.rotButton.clicked.connect(self.rotate)
        # Adiciona os widgets ao layout
        self.rotGroupBox.layout().addWidget(self.degSpinBox, 1, 0)
        self.rotGroupBox.layout().addWidget(degLabel, 1, 1)
        self.rotGroupBox.layout().addWidget(self.rotButton, 2, 0, 1, 3)
        # Adiciona um stretch vertical no grupo
        self.rotGroupBox.layout().setRowStretch(3, 1)
        self.setCentralWidget(widget)

    def rotate(self):
        # Obtém o eixo de rotação
        deg = radians(self.degSpinBox.value())
        if self.radioX.isChecked():
            self.ramp.rotate_x(deg)
        elif self.radioY.isChecked():
            self.ramp.rotate_y(deg)
        elif self.radioZ.isChecked():
            self.ramp.rotate_z(deg)
        # Atualiza a imagem
        self.imgLabel.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(self.ramp.to_img())))