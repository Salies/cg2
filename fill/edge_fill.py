import numpy as np
from PIL import Image, ImageDraw

# Abrindo a imagem
im = Image.open('img/edge.png')

# Definindo o bounding-box
# x-min, y-min, x-max, y-max
bb = [(14, 35), (184, 165)]

# Draw a rectangle in the bounding box area
im2 = Image.new('RGBA', (200, 200))
img1 = ImageDraw.Draw(im2)
img1.rectangle(bb, fill =(255, 0, 0))

im3 = Image.blend(im, im2, 0.5)

im3.show()