import math
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QBrush
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy
from PIL import Image, ImageDraw
from collections import namedtuple
from operator import attrgetter
from typing import List
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.patches import Circle



class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 300)
        self.path = []
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.path.append((event.x(), event.y()))
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.path.append((event.x(), event.y()))
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(Qt.black)
        painter.setBrush(brush)
        for i in range(len(self.path) - 1):
            painter.drawLine(self.path[i][0], self.path[i][1],
                             self.path[i + 1][0], self.path[i + 1][1])

Point = namedtuple('Point', ['x', 'y'])
def convex_hull(points: List[Point]) -> List[Point]:
        def cross(o, a, b):
            return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

        points = sorted(points, key=attrgetter('x'))
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)

        return lower[:-1] + upper[:-1]

def rotate(p, theta):
    x, y = p
    return x * math.cos(theta) - y * math.sin(theta), x * math.sin(theta) + y * math.cos(theta)

matrix_rotacao: List[List[float]] = [
    [math.cos(45 * math.pi/180), -math.sin(45 * math.pi/180), 0],
    [math.sin(45 * math.pi/180), math.cos(45 * math.pi/180), 0],
    [0, 0, 1]
]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle("Drawing Canvas")
        self.canvas = Canvas()
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_canvas)
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.ok_canvas)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.ok_button)
        self.setLayout(layout)
        self.eixo = 150


    # Inserts a straight vertical line on the middle of the window:
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(Qt.black)
        painter.setBrush(brush)
        painter.drawLine(self.eixo, 0, self.eixo, 300)
        
    

    def clear_canvas(self):
        self.canvas.path = []
        self.canvas.update()

    def ok_canvas(self):
        traco = self.canvas.path
        points = [Point(x, y) for x, y in traco]
        altura = 300
        largura = 300
        img = Image.new('RGB', (largura, altura), color = 'white')
        draw = ImageDraw.Draw(img)
        saida = convex_hull(points)
        for i in range(len(points) - 1):
            draw.line((points[i].x + float(self.eixo) * math.cos(45 * math.pi/180), points[i].y + float(self.eixo)*math.sin(45*math.pi/180)), fill='black', width=1)
        img.show()

        rotacionado = [[]]
        rotacionado1 = [[]]
        for i in range(len(traco) - 1):
            rotacionado.append(rotate(traco[i], 45 * math.pi/180))
            for j in range(len(traco[i])):
                rotacionado1.append(traco[i][j] * matrix_rotacao[i][j])
        print(rotacionado)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(rotacionado[0], rotacionado[1], rotacionado[2])
        plt.show()



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
