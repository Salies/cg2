from Illumination import Illumination
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QGroupBox, QGridLayout, QPushButton, QDoubleSpinBox, QRadioButton
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt
from PIL import ImageQt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Iluminação")
        self.setWindowIcon(QIcon("ico/BTLPANEL.BIN_1.png"))

        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QGridLayout()
        widget.setLayout(layout)
    
        self.ilu = Illumination()
        # Pegando uma imagem padrão sem iluminação
        im = self.ilu.no_ilu()
        # Criando um label para exibir a imagem
        self.label = QLabel()
        # Criando um pixmap a partir da imagem
        pixmap = QPixmap.fromImage(ImageQt.ImageQt(im))
        # Colocando o pixmap no label
        self.label.setPixmap(pixmap)

        # Adcionando o label ao layout
        layout.addWidget(self.label, 0, 0, 5, 2)

        # Radio button de iluminação
        self.ad = QRadioButton("Ambiente + difusa")
        self.ad.setChecked(True)
        self.ads = QRadioButton("Ambiente + difusa + especular")

        # Criando um grupo para os radio buttons
        group_ilu = QGroupBox("Tipo de iluminação")
        layout.addWidget(group_ilu, 0, 3)
        layout_ilu = QGridLayout()
        group_ilu.setLayout(layout_ilu)
        layout_ilu.addWidget(self.ad, 0, 0)
        layout_ilu.addWidget(self.ads, 0, 1)

        # Criando as spinboxes
        self.ia = QDoubleSpinBox()
        self.ia.setRange(0, 1000)
        self.ia.setValue(0.8)
        self.ka = QDoubleSpinBox()
        self.ka.setRange(0, 1000)
        self.ka.setValue(0.5)
        self.il = QDoubleSpinBox()
        self.il.setRange(0, 1000)
        self.il.setValue(0.8)
        self.kd_sphere = QDoubleSpinBox()
        self.kd_sphere.setRange(0, 1000)
        self.kd_sphere.setValue(0.3)
        self.kd_plane = QDoubleSpinBox()
        self.kd_plane.setRange(0, 1000)
        self.kd_plane.setValue(0.7)
        self.ks_sphere = QDoubleSpinBox()
        self.ks_sphere.setRange(0, 1000)
        self.ks_sphere.setValue(0.8)
        self.ks_plane = QDoubleSpinBox()
        self.ks_plane.setRange(0, 1000)
        self.ks_plane.setValue(0.4)
        self.n = QDoubleSpinBox()
        self.n.setRange(0, 1000)
        self.n.setValue(2)
        self.k = QDoubleSpinBox()
        self.k.setRange(0, 1000)
        self.k.setValue(2)

        # Grupo: constantes objetos
        group_const_obj = QGroupBox("Constantes (objetos)")
        layout.addWidget(group_const_obj, 1, 3)
        layout_const_obj = QGridLayout()
        aux = QLabel("Kd (esfera):")
        aux.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        group_const_obj.setLayout(layout_const_obj)
        layout_const_obj.addWidget(aux, 0, 0)
        layout_const_obj.addWidget(self.kd_sphere, 0, 1)
        aux = QLabel("Kd (plano):")
        aux.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout_const_obj.addWidget(aux, 0, 2)
        layout_const_obj.addWidget(self.kd_plane, 0, 3)
        aux = QLabel("Ks (esfera):")
        aux.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout_const_obj.addWidget(aux, 1, 0)
        layout_const_obj.addWidget(self.ks_sphere, 1, 1)
        aux = QLabel("Ks (plano):")
        aux.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout_const_obj.addWidget(aux, 1, 2)
        layout_const_obj.addWidget(self.ks_plane, 1, 3)

        # Grupo: constantes luz
        group_const_luz = QGroupBox("Constantes (ambiente e difusa)")
        layout.addWidget(group_const_luz, 2, 3)
        layout_const_luz = QGridLayout()
        group_const_luz.setLayout(layout_const_luz)
        aux = QLabel("Ia:")
        aux.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout_const_luz.addWidget(aux, 0, 0)
        layout_const_luz.addWidget(self.ia, 0, 1)
        aux = QLabel("Ka:")
        aux.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout_const_luz.addWidget(aux, 0, 2)
        layout_const_luz.addWidget(self.ka, 0, 3)
        aux = QLabel("Il:")
        aux.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout_const_luz.addWidget(aux, 0, 4)
        layout_const_luz.addWidget(self.il, 0, 5)

        # Grupo: constantes especular
        group_const_especular = QGroupBox("Constantes (especular)")
        layout.addWidget(group_const_especular, 3, 3)
        layout_const_especular = QGridLayout()
        group_const_especular.setLayout(layout_const_especular)
        aux = QLabel("K:")
        aux.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout_const_especular.addWidget(aux, 0, 0)
        layout_const_especular.addWidget(self.k, 0, 1)
        aux = QLabel("n:")
        aux.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout_const_especular.addWidget(aux, 0, 2)
        layout_const_especular.addWidget(self.n, 0, 3)

        # Botão de iluminar
        ilu = QPushButton("Iluminar")
        layout.addWidget(ilu, 4, 3)
        ilu.clicked.connect(self.illuminate)

    def illuminate(self):
        if self.ad.isChecked():
            im = self.ilu.ilu_a(self.ia.value(), self.ka.value(), self.il.value(), self.kd_sphere.value(), self.kd_plane.value())
        elif self.ads.isChecked():
            im = self.ilu.ilu_b(
                self.ia.value(), self.ka.value(), self.il.value(), self.k.value(), self.n.value(),
                self.kd_sphere.value(), self.kd_plane.value(), 
                self.ks_sphere.value(), self.ks_plane.value()
            )
        self.label.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(im)))