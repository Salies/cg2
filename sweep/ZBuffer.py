import numpy as np
from PIL import Image

class ZBuffer:
    def __init__(self, size) -> None:
        x, y = size
        # Matriz da imagem
        self.mm = np.full((x, y), 255)
        # Matriz do Z-Buffer -- float 32 me parece ser o suficiente
        self.buffer = np.full((x, y), np.inf, dtype=np.float32)
    
    def set_point(self, x, y, z, color):

        x = np.round(x).astype(int)
        y = np.round(y).astype(int)

        if x < 0 or x > 399 or y < 0 or y > 399:
            return

        if z >= self.buffer[y, x]:
            return
        self.buffer[y, x] = z
        self.mm[y, x] = color

    def to_img(self):
        im = Image.fromarray(self.mm)
        return im