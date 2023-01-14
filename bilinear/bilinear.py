import numpy as np
from PIL import Image
# importando o pprint
import pprint

# Essa função recebe os quatro pontos do plano e retorna
# os pontos que farão a composição deste plano na imagem,
# de acordo com a modelagem via superfície bilinear.
def bilinear(p00, p01, p10, p11):
    points = []
    for u in np.arange(0, 1, 0.01):
        for v in np.arange(0, 1, 0.01):
            p = p00 * (1 - u) * (1 - v) + p01 * (1 - u) * v + p10 * u * (1 - v) + p11 * u * v
            points.append(p)
    # Como x e y precisam ser inteiros para serem usados como índices,
    # arrendodamos seus valores e retiramos os pontos duplicados.
    points = np.array(points)
    # Arredonda apenas os valores de x e y
    points[:, 0] = np.round(points[:, 0])
    points[:, 1] = np.round(points[:, 1])
    # Remove duplicados
    points = np.unique(points, axis=0)
    return points

# Uma versão ligeiramente modificada da classe ZBuffer
class ZBuffer:
    def __init__(self, size, offsetX, offsetY) -> None:
        self.sizeX, self.sizeY = size
        self.offsetx = offsetX
        self.offsety = offsetY
        # Matriz da imagem
        self.mm = np.zeros((self.sizeX, self.sizeY, 3), dtype=np.uint8)
        # Matriz do Z-Buffer -- float 32 me parece ser o suficiente
        self.buffer = np.full((self.sizeX, self.sizeY), np.inf, dtype=np.float32)
    
    def set_point(self, x, y, z, color):
        x, y = x + self.offsetX, self.offsetY - y
        # Invertendo x e y pois os objetos são dados em
        # um plano cartesiano, mas aqui trata-se de uma imagem.
        # Checando se o ponto está dentro da imagem
        if x < 0 or x > (self.sizeX  - 1) or y < 0 or y > (self.sizeY - 1):
            return

        if z >= self.buffer[y, x]:
            return
        self.buffer[y, x] = z
        self.mm[y, x] = color

    def to_img(self):
        im = Image.fromarray(self.mm)
        return im

# Classe para construção dos objetos e geração da imagem
class Ramp:
    def __init__(self):
        # Verde (baixo)
        gd = [
            [0, 0, 0],
            [20, 0, 0],
            [0, 20, 0],
            [20, 20, 0]
        ]
        # Verde (cima)
        gu = [
            [0, 0, 80],
            [20, 0, 80],
            [0, 40, 80],
            [20, 40, 80]
        ]
        # Verde (frente)
        gf = [
            [0, 0, 0],
            [20, 0, 0],
            [0, 0, 80],
            [20, 0, 80]
        ]
        # Azul
        az = [
            [20, 0, 80],
            [20, 40, 80],
            [100, 0, 0],
            [100, 40, 0]
        ]
        # Amarelo
        yl = [
            [20, 40, 0],
            [20, 40, 0],
            [20, 0, 80],
            [20, 40, 80]
        ]
        # Vermelho
        rd = [
            [20, 0, 0],
            [100, 0, 0],
            [20, 40, 0],
            [100, 40, 0]
        ]
        # Marrom
        br = [
            [100, 0, 0],
            [120, 0, 0],
            [100, 40, 0],
            [120, 40, 0]
        ]
        # Monta um matriz com os pontos básicos (antes do processamento de superfície bilinear)
        basic_points = np.array([gd, gu, gf, az, yl, rd, br])
        # Neste vetor temos as cores de cada um, para montar uma estrutura de dados
        # mais fácil de ser processada.
        colors = [
            [0, 255, 0],
            [0, 255, 0],
            [0, 255, 0],
            [0, 0, 255],
            [255, 255, 0],
            [255, 0, 0],
            [150, 75, 0]
        ]
        # Agora processa cada um deles, e coloca num dict com cor e pontos
        self.points = [{'color': colors[i], 'points': bilinear(*basic_points[i])} for i in range(len(basic_points))]

    def test(self):
        pprint.pprint(self.points)

t = Ramp()
t.test()

'''
# Teste
ret_test = [
    (0, 0, 0),
    (20, 0, 0),
    (0, 20, 0),
    (20, 20, 0)
]

ret_test2 = [
    [20, 0, 80],
    [20, 40, 80],
    [100, 0, 0],
    [100, 40, 0]
]

ret_test = np.array(ret_test2)

print(bilinear(ret_test[0], ret_test[1], ret_test[2], ret_test[3]).shape)
'''