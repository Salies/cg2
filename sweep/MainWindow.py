from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QLabel
from PySide6.QtGui import QPaintDevice, QPainter, QPen, QBrush, QColor, QImage, QPixmap, QPainterPath
from Canvas import Canvas

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

    def setPath(self, path):
        self.path = path
        print(path)