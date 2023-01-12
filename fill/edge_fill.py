import numpy as np
from PIL import Image, ImageDraw

class EdgeFill:
    def __init__(self):
        # Definindo o polígono
        self.edges = [
            [(16, 180), (180, 180)],
            [(180, 86), (180, 180)],
            [(120, 120), (180, 86)],
            [(16, 36), (120, 120)],
            [(16, 36), (16, 180)],
        ]

        # Definindo o bounding-box
        # x-min, y-min, x-max, y-max
        self.bb = [(12, 30), (184, 184)]

        # Desenha a imagem base
        self.base_im = Image.new('RGB', (200, 200), (250, 218, 94))

    def get_img(self):
        im = self.base_im.copy()
        draw = ImageDraw.Draw(im)
        for edge in self.edges:
            draw.line(edge, fill=(0, 0, 0), width=1)
        return im

    def fill(self):
        for edge in self.edges:
            x1, y1 = edge[0]
            x2, y2 = edge[1]
            if y1 == y2:
                continue
            if y1 > y2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            # Now we have y1 < y2
            for y in range(y1, y2 + 1):
                # Here we can't just use x1
                # because the line may not be fully vertical
                x = np.round(x1 + (x2 - x1) * (y - y1) / (y2 - y1)).astype(int)
                # Invert every pixel to the right of the edge
                # No need to go until the max x, since the bounding box
                # will take care of that
                for x in range(x, self.bb[1][0] + 1):
                    r, g, b = self.base_im.getpixel((x, y))
                    self.base_im.putpixel((x, y), (255 - r, 255 - g, 255 - b))