import numpy as np
from PIL import Image
import sys

sys.setrecursionlimit(10000)

'''im = Image.open('Testar_FloodFill.bmp').convert('RGB')
a = np.array(im)

def flood_fill(img, x, y, target_color, paint_color):
    img[y, x] = paint_color

    if x > 0 and np.array_equal(img[y, x-1], target_color) and np.array_equal(img[y, x-1], paint_color) == False:
        flood_fill(img, x-1, y, target_color, paint_color)
    if x < img.shape[1]-1 and np.array_equal(img[y, x+1], target_color) and np.array_equal(img[y, x+1], paint_color) == False:
        flood_fill(img, x+1, y, target_color, paint_color)
    if y > 0 and np.array_equal(img[y-1, x], target_color) and np.array_equal(img[y-1, x], paint_color) == False:
        flood_fill(img, x, y-1, target_color, paint_color)
    if y < img.shape[0]-1 and np.array_equal(img[y+1, x], target_color) and np.array_equal(img[y+1, x], paint_color) == False:
        flood_fill(img, x, y+1, target_color, paint_color)

flood_fill(a, 0, 0, (255, 255, 255), (255, 0, 0))

im = Image.fromarray(a)
im.save('Testar_FloodFill3.bmp')'''

'''matrix = [[255, 255, 0, 255, 255, 0],
          [255, 0, 0, 255, 0, 0],
          [0, 255, 0, 255, 255, 0],
          [0, 255, 0, 255, 0, 0],
          [255, 255, 0, 255, 255, 255],
          [255, 0, 0, 255, 255, 0]]

m = np.array(matrix)'''

im = Image.open('Testar_FloodFill.bmp').convert('L')
m = np.array(im)

def teste(a, x, y):
    a[x, y] = 120

    if x > 0 and a[x - 1, y] == 255:
        teste(a, x - 1, y)
    if x < a.shape[0] - 1 and a[x + 1, y] == 255:
        teste(a, x + 1, y)
    if y > 0 and a[x, y - 1] == 255:
        teste(a, x, y - 1)
    if y < a.shape[1] - 1 and a[x, y + 1] == 255:
        teste(a, x, y + 1)

teste(m, 0, 0)
print(m)