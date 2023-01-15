import numpy as np
from PIL import Image, ImageDraw
from ZBuffer import ZBuffer

def rotate_point(p, g):
    T = np.array([
        [np.cos(g), 0, np.sin(g), 0],
        [0, 1, 0, 0],
        [-np.sin(g), 0, np.cos(g), 0],
        [0, 0, 0, 1]
    ])
    # x, y, z, 1 = x, y, 0, 1
    p = np.array([*p, 0, 1])
    p = p @ T
    return p[:3]

# White image with a vertical black line in the middle
# Can be a gray image because where only using black and white
img = Image.new('L', (401, 400), 255)
draw = ImageDraw.Draw(img)
draw.line((200, 0, 200, 400), fill=0, width=1)

arr = np.full((400, 401), 255)
img = Image.open('sweeptest.png').convert('L')
# Isolate the black pixels on the right side of the image
# and mark them in the array
for i in range(400):
    for j in range(201, 401):
        if img.getpixel((j, i)) == 0:
            arr[i][j] = 0

'''
            circleCoords.push({x: x, y: coords[i].y, z: z});
            circleCoords.push({x: z, y: coords[i].y, z: x});
            circleCoords.push({x: -x, y: coords[i].y, z: z});
            circleCoords.push({x: -z, y: coords[i].y, z: x});
            circleCoords.push({x: -x, y: coords[i].y, z: -z});
            circleCoords.push({x: -z, y: coords[i].y, z: -x});
            circleCoords.push({x: x, y: coords[i].y, z: -z});
            circleCoords.push({x: z, y: coords[i].y, z: -x});
'''

# This was just a test. Now suppose this array is what the user draw.
# For each pixel, we need to check if it is black and if it is, we rotate
# the pixel 360 degrees on the y axis and draw each rotation.
zb = ZBuffer((401, 400))
for i in range(0, 400, 5):
    for j in range(400):
        if arr[i][j] == 0:
            r = np.abs(200 - j)
            x = 0
            z = r
            d  = 3 - 2 * r
            while x <= z:
                if d < 0:
                    d = d + 4 * x + 6
                else:
                    d = d + 4 * (x - z) + 10
                    z = z - 1
                x = x + 1
                # Draw the pixel in the array
                arr[i][x + 200] = 0
                arr[i][200 - x] = 0
                arr[i][z + 200] = 0
                arr[i][200 - z] = 0
                # Draw the pixel in the ZBuffer
                zb.set_point(x + 200, i, z, 0)
                zb.set_point(z + 200, i, x, 0)
                zb.set_point(-x + 200, i, z, 0)
                zb.set_point(-z + 200, i, x, 0)
                zb.set_point(-x + 200, i, -z, 0)
                zb.set_point(-z + 200, i, -x, 0)
                zb.set_point(x + 200, i, -z, 0)
                zb.set_point(z + 200, i, -x, 0)

zb.to_img().show()