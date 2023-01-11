import numpy as np
from PIL import Image
import sys

im = Image.open('Testar_FloodFill.bmp').convert('RGB')
m = np.array(im)

def flood_fill(img, xo, yo, paint_color, target_color):
    if paint_color == target_color:
        return

    img[xo, yo] = paint_color

    stack = [(xo, yo)]
    while stack:
        x, y = stack.pop()
        if x > 0 and np.array_equal(img[x-1, y], target_color):
            img[x-1, y] = paint_color
            stack.append((x-1, y))
        if x < img.shape[0]-1 and np.array_equal(img[x+1, y], target_color):
            img[x+1, y] = paint_color
            stack.append((x+1, y))
        if y > 0 and np.array_equal(img[x, y-1], target_color):
            img[x, y-1] = paint_color
            stack.append((x, y-1))
        if y < img.shape[1]-1 and np.array_equal(img[x, y+1], target_color):
            img[x, y+1] = paint_color
            stack.append((x, y+1))

flood_fill(m, 100, 60, [255, 100, 0], [255, 255, 255])
Image.fromarray(m).show()