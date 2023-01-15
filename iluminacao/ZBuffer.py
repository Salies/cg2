import numpy as np
from PIL import Image

# Mesma classe de ZBuffer do trabalho dos objetos
# Copiada aqui por conveniência
class ZBuffer:
    def __init__(self, size, offset) -> None:
        x, y = size
        self.offset = offset
        # Matriz da imagem
        self.mm = np.zeros((x, y, 3), dtype=np.uint8)
        # Matriz do Z-Buffer -- float 32 me parece ser o suficiente
        self.buffer = np.full((x, y), np.inf, dtype=np.float32)
    
    def set_point(self, x, y, z, color):
        x, y = np.round(x + self.offset).astype(int), np.round(self.offset - y).astype(int)
        # Invertendo x e y pois os objetos são dados em
        # um plano cartesiano, mas aqui trata-se de uma imagem.
        # Checando se o ponto está dentro da imagem
        if x < 0 or x > 299 or y < 0 or y > 299:
            return

        if z >= self.buffer[y, x]:
            return
        self.buffer[y, x] = z
        self.mm[y, x] = color

    def to_img(self):
        im = Image.fromarray(self.mm)
        return im