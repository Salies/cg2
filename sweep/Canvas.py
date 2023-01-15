from PySide6 import QtGui, QtCore, QtWidgets

class Canvas(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Canvas, self).__init__()
        self.parent = parent
        self.setFixedSize(401, 400)
        self.setWindowTitle('Draw')
        self.brush_size = 1
        self.brush_color = QtCore.Qt.black
        self.last_point = QtCore.QPoint()
        self.path = QtGui.QPainterPath()
        # Coloca a imagem com o eixo de fundo
        self.image = QtGui.QImage("img/sweep-bg.png")
        self.scaled_image = self.image.scaled(self.size())
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setBrush(QtGui.QPalette.Window, QtGui.QBrush(self.scaled_image))
        self.setPalette(p)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(self.brush_color, self.brush_size, QtCore.Qt.SolidLine))
        painter.drawPath(self.path)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.path = QtGui.QPainterPath()
            self.path.addRect(event.pos().x(), event.pos().y(), self.brush_size, self.brush_size)
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() and QtCore.Qt.LeftButton:
            self.path.addRect(event.pos().x(), event.pos().y(), self.brush_size, self.brush_size)
            self.update()

    def mouseReleaseEvent(self, event):
        # Extraindo todos os pontos do desenho
        points = []
        for i in range(self.path.elementCount()):
            el = self.path.elementAt(i)
            if el.type == QtGui.QPainterPath.MoveToElement:
                points.append((el.x, el.y))
            elif el.type == QtGui.QPainterPath.LineToElement:
                points.append((el.x, el.y))
        # Enviando os pontos para o MainWindow
        self.parent.setPath(points)