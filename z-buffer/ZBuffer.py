import numpy as np
from PIL import Image

class ZBuffer:
    def __init__(self, size, offset) -> None:
        x, y = size
        self.offset = offset
        # Matriz da imagem
        self.mm = np.zeros((x, y, 3), dtype=np.uint8)
        # Matriz do Z-Buffer -- float 32 me parece ser o suficiente
        self.buffer = np.full((x, y), np.inf, dtype=np.float32)
    
    def set_point(self, x, y, z, color):
        x, y = x + self.offset, self.offset - y
        # Invertendo x e y pois os objetos são dados em
        # um plano cartesiano, mas aqui trata-se de uma imagem.
        if x > 300 or y < 0:
            return

        if z >= self.buffer[y, x]:
            return
        self.buffer[y, x] = z
        self.mm[y, x] = color

    def to_img(self):
        im = Image.fromarray(self.mm)
        return im