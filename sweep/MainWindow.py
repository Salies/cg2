from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QLabel
from PySide6.QtGui import QPaintDevice, QPainter, QPen, QBrush, QColor, QImage, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Varredura rotacional")
        widget = QWidget()
        self.setCentralWidget(widget)
        self.layout = QHBoxLayout()
        widget.setLayout(self.layout)
        self.createCanvas()

    # Cria a tela de desenho
    def createCanvas(self):
        self.canvas = QLabel()
        self.canvas.setFixedSize(401, 400)
        # Load background image
        self.canvas.setPixmap(QPixmap("img/sweep-bg.png"))
        self.layout.addWidget(self.canvas)
        # When use click, draw a point
        self.canvas.mousePressEvent = self.beginDraw
        self.canvas.mouseMoveEvent = self.draw
        self.canvas.mouseReleaseEvent = self.endDraw

    # Desenha o ponto na tela
    def beginDraw(self, event):
        x, y = event.pos().x(), event.pos().y()
        self.isDrawing = True
        print(x, y)

    def draw(self, event):
        if not self.isDrawing:
            return
        x, y = event.pos().x(), event.pos().y()
        print(x, y)

    def endDraw(self, event):
        self.isDrawing = False