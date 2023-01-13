import numpy as np

# Vizinhança-4
def flood_fill(img, xo, yo, paint_color, target_color):
    if paint_color == target_color:
        return

    img[xo, yo] = paint_color

    stack = [(xo, yo)]
    while stack:
        x, y = stack.pop()
        # np.array_equal é uma instrução que compara dois arrays, no caso, duas cores
        # de resto, é um algoritmo comum de flood fill por pilha (Python é péssimo para recursão).
        # O mesmo vale para a versão com vizinhança-8.
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

# Vizinhança-8
def flood_fill_eight(img, xo, yo, paint_color, target_color):
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
        if x > 0 and y > 0 and np.array_equal(img[x-1, y-1], target_color):
            img[x-1, y-1] = paint_color
            stack.append((x-1, y-1))
        if x > 0 and y < img.shape[1]-1 and np.array_equal(img[x-1, y+1], target_color):
            img[x-1, y+1] = paint_color
            stack.append((x-1, y+1))
        if x < img.shape[0]-1 and y > 0 and np.array_equal(img[x+1, y-1], target_color):
            img[x+1, y-1] = paint_color
            stack.append((x+1, y-1))
        if x < img.shape[0]-1 and y < img.shape[1]-1 and np.array_equal(img[x+1, y+1], target_color):
            img[x+1, y+1] = paint_color
            stack.append((x+1, y+1))
