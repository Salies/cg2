import numpy as np
from PIL import Image
from ZBuffer import ZBuffer

# TODO: melhorar performance da esfera

# Funções auxiliares para construção dos objetos
# azul
curve = lambda x, y: x ** 2 + y
# vermelho
plane = lambda x, y: 3 * x - 2 * y + 5
# amarelo
cilinder = lambda t, a: (30 + np.cos(a) * t, 50 + np.sin(a) * t, 10 + t)
# verde
sphere = lambda a, b: (
    100 + 30 * np.cos(a) * np.cos(b), 
    50 + 30 * np.cos(a) * np.sin(b), 
    20 + 30 * np.sin(a)
)

zb = ZBuffer((300, 300), 150)

points = []
colors = []

# Construindo os objetos
# Calha azul
for x in range(10, 31):
    for y in range(20, 41):
        points.append((x, y, curve(x, y)))
        colors.append((0, 0, 255))

# Plano vermelho
for x in range(50, 101):
    for y in range(30, 81):
        points.append((x, y, plane(x, y)))
        colors.append((255, 0, 0))

# Cilindro amarelo
cilinder_points = []
for a in np.linspace(0, 2 * np.pi, 620):
    for t in range(0, 51):
        x, y, z = cilinder(t, a)
        x, y = np.round(x).astype(int), np.round(y).astype(int)
        cilinder_points.append((x, y, z))
cilinder_points = list(set(cilinder_points))
for x, y, z in cilinder_points:
    points.append((x, y, z))
    colors.append((255, 255, 0))

# Esfera verde
sphere_points = []
for a in np.linspace(0, 2 * np.pi, 200):
    # TODO: perguntar: pode ser assim né?
    for b in np.linspace(0, np.pi, 200):
        x, y, z = sphere(a, b)
        x, y = np.round(x).astype(int), np.round(y).astype(int)
        sphere_points.append((x, y, z))
sphere_points = list(set(sphere_points))
for x, y, z in sphere_points:
    points.append((x, y, z))
    colors.append((0, 255, 0))

# Cubo branco
for x in range(-20, 21):
    for y in range(-20, 21):
        points.append((x, y, -20))
        points.append((x, y, 20))
        points.append((x, 20, y))
        points.append((x, -20, y))
        points.append((20, x, y))
        points.append((-20, x, y))
        colors += [(255, 255, 255)] * 6

# Print the points, except last item
#print(points)
points = np.array(points).astype(int)

# Rotacionando 30 graus em torno de x
graus = np.radians(30)
T = np.array([
    [1, 0, 0, 0],
    [0, np.cos(graus), -np.sin(graus), 0],
    [0, np.sin(graus), np.cos(graus), 0],
    [0, 0, 0, 1]
])

points = np.c_[points, np.ones(points.shape[0])].astype(int)

points = np.round(points @ T).astype(int)

points = points[:, :-1]

for i in range(len(points)):
    x, y, z = points[i]
    color = colors[i]
    zb.set_point(x, y, z, color)

zb.save('z-buffer2.png')