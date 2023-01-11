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
        x, y = x + self.offset, y + self.offset
        if z >= self.buffer[x, y]:
            return
        self.buffer[x, y] = z
        self.mm[x, y] = color

    def save(self, filename):
        im = Image.fromarray(self.mm)
        im.save(filename)