from PySide6 import QtGui, QtCore, QtWidgets

class DrawWidget(QtWidgets.QWidget):
    def __init__(self):
        super(DrawWidget, self).__init__()
        self.setFixedSize(401, 400)
        self.setWindowTitle('Draw')
        self.brush_size = 1
        self.brush_color = QtCore.Qt.black
        self.last_point = QtCore.QPoint()
        self.path = QtGui.QPainterPath()

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
        pass