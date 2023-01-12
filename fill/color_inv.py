import numpy as np
from PIL import Image, ImageDraw

# Definindo o polígono
edges = [
    [(16, 180), (180, 180)],
    [(180, 86), (180, 180)],
    [(120, 120), (180, 86)],
    [(16, 36), (120, 120)],
    [(16, 36), (16, 180)],
]

# Definindo o bounding-box
# x-min, y-min, x-max, y-max
bb = [(12, 30), (184, 184)]

# For each edge, draw a line
im = Image.new('RGB', (200, 200), (250, 218, 94))

# Now for the color inversion algorithm
# For every edge of the polygon, check if it's horiziontal.
# If it's NOT horizontal, than for each line in the edge,
# invert every pixel to the right of the edge.
#edges_test = [edges[1], edges[2]]
for edge in edges:
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
        for x in range(x, bb[1][0] + 1):
            r, g, b = im.getpixel((x, y))
            im.putpixel((x, y), (255 - r, 255 - g, 255 - b))

draw = ImageDraw.Draw(im)
for edge in edges:
    draw.line(edge, fill=(0, 0, 0), width=1)

im.show()