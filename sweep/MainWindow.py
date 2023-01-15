from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QPixmap, QFont
from Canvas import Canvas
import numpy as np
from sweep import sweep

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Varredura rotacional")
        widget = QWidget()
        self.setCentralWidget(widget)
        self.layout = QHBoxLayout()
        widget.setLayout(self.layout)
        draw = Canvas(self)
        self.layout.addWidget(draw)
        # Adicionando um botão para executar a varredura
        font = QFont()
        font.setPointSize(20)
        btn = QPushButton("🡆")
        btn.setFont(font)
        btn.clicked.connect(self.doSweep)
        self.layout.addWidget(btn)
        # Adicionando uma label para receber a imagem resultante da varredura
        self.label = QLabel()
        self.label.setFixedSize(401, 400)
        self.layout.addWidget(self.label)

    def setPath(self, path):
        # Tratando os pontos (apenas os pares únicos)
        path = np.unique(np.array(path, dtype=int), axis=0)
        self.path = path

    def doSweep(self):
        # Executando a varredura
        img = sweep(self.path)
        # Exibindo a imagem resultante
        self.label.setPixmap(QPixmap.fromImage(img))