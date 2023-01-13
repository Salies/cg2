import numpy as np
from ZBuffer import ZBuffer
from numba import njit

# azul
@njit
def curve(x, y):
    return x ** 2 + y

# vermelho
@njit
def plane(x, y):
    return 3 * x - 2 * y + 5

# amarelo
@njit
def cilinder(t, a):
    return 30 + np.cos(a) * t, 50 + np.sin(a) * t, 10 + t

# verde
@njit
def sphere(a, b):
    return 100 + 30 * np.cos(a) * np.cos(b), 50 + 30 * np.cos(a) * np.sin(b), 20 + 30 * np.sin(a)

# Função para construir os objetos
@njit
def build_objects():
    points = []
    colors = []

    # Construindo os objetos
    # Calha azul
    for x in range(10, 31):
        for y in range(20, 41):
            points.append((x, y, curve(x, y)))
            colors.append((0, 0, 255))

    # Plano vermelho
    for x in range(50, 101):
        for y in range(30, 81):
            points.append((x, y, plane(x, y)))
            colors.append((255, 0, 0))

    # Cilindro amarelo
    cilinder_points = []
    for a in np.linspace(0, 2 * np.pi, 620):
        for t in range(0, 51):
            x, y, z = cilinder(t, a)
            x, y = int(np.round(x)), int(np.round(y))
            cilinder_points.append((x, y, z))
    cilinder_points = list(set(cilinder_points))
    for x, y, z in cilinder_points:
        points.append((x, y, z))
        colors.append((255, 255, 0))

    # Esfera verde
    sphere_points = []
    for a in np.linspace(0, 2 * np.pi, 200):
        for b in np.linspace(0, np.pi, 200):
            x, y, z = sphere(a, b)
            x, y = int(np.round(x)), int(np.round(y))
            sphere_points.append((x, y, z))
    # Retira possíveis pontos repetidos, para economizar
    # no desenho depois.
    sphere_points = list(set(sphere_points))
    for x, y, z in sphere_points:
        points.append((x, y, z))
        colors.append((0, 255, 0))

    # Cubo branco
    for x in range(-20, 21):
        for y in range(-20, 21):
            points.append((x, y, -20))
            points.append((x, y, 20))
            points.append((x, 20, y))
            points.append((x, -20, y))
            points.append((20, x, y))
            points.append((-20, x, y))
            colors += [(255, 255, 255)] * 6

    points = np.array(points)
    # Transforma os pontos em coordenadas homogêneas
    points = np.hstack((points, np.ones((points.shape[0], 1))))

    return points, colors

# Classe para "montar" os objetos a serem exibidos com o Z-Buffer
# e rotacioná-los de acordo com a entrada do usuário.
# A classe em si só chamada uma série de funções externas @njit-adas, para
# melhoria de performance.

class Objects:
    def __init__(self):
        self.points, self.colors = build_objects()

    # Desenha os pontos usando o Z-Buffer
    def to_img(self):
        # Cria um Z-Buffer
        zb = ZBuffer((300, 300), 150)
        # Desenha os objetos na imagem, ponto a ponto
        for i in range(len(self.points)):
            x, y, z = self.points[i]
            color = self.colors[i]
            zb.set_point(x, y, z, color)
        # Retorna a imagem
        return zb.to_img()

    # Rotaciona os objetos em torno do eixo x por g graus radianos
    def rotate_x(self, g):
        # Matriz de rotação
        T = np.array([
            [1, 0, 0, 0],
            [0, np.cos(g), -np.sin(g), 0],
            [0, np.sin(g), np.cos(g), 0],
            [0, 0, 0, 1]
        ])
        # Aplica a rotação
        self.points = self.points @ T

    # Rotaciona os objetos em torno do eixo y
    def rotate_y(self, g):
        # Matriz de rotação
        T = np.array([
            [np.cos(g), 0, np.sin(g), 0],
            [0, 1, 0, 0],
            [-np.sin(g), 0, np.cos(g), 0],
            [0, 0, 0, 1]
        ])
        # Aplica a rotação
        self.points = self.points @ T

    # Rotaciona os objetos em torno do eixo z
    def rotate_z(self, g):
        # Matriz de rotação
        T = np.array([
            [np.cos(g), -np.sin(g), 0, 0],
            [np.sin(g), np.cos(g), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
        # Aplica a rotação
        self.points = self.points @ T