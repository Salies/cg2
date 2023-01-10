import numpy as np
from PIL import Image
import sys

im = Image.open('Testar_FloodFill.bmp').convert('L')
m = np.array(im)

def flood_fill(img, x, y, paint_color, target_color):
    img[x, y] = paint_color

    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if x > 0 and img[x-1, y] == 255:
            img[x-1, y] = target_color
            stack.append((x-1, y))
        if x < img.shape[0]-1 and img[x+1, y] == 255:
            img[x+1, y] = target_color
            stack.append((x+1, y))
        if y > 0 and img[x, y-1] == 255:
            img[x, y-1] = target_color
            stack.append((x, y-1))
        if y < img.shape[1]-1 and img[x, y+1] == 255:
            img[x, y+1] = target_color
            stack.append((x, y+1))

flood_fill(m, 100, 60, 10, 100)
Image.fromarray(m).show()