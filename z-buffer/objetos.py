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

# Construindo os objetos
# Calha azul
for x in range(10, 31):
    for y in range(20, 41):
        zb.set_point(x, y, curve(x, y), (0, 0, 255))

# Plano vermelho
for x in range(50, 101):
    for y in range(30, 81):
        zb.set_point(x, y, plane(x, y), (255, 0, 0))

# Cilindro amarelo
cilinder_points = []
for a in np.linspace(0, 2 * np.pi, 1000):
    for t in range(0, 51):
        x, y, z = cilinder(t, a)
        x, y = np.round(x).astype(int), np.round(y).astype(int)
        cilinder_points.append((x, y, z))
cilinder_points = list(set(cilinder_points))
for x, y, z in cilinder_points:
    zb.set_point(x, y, z, (255, 255, 0))

# Esfera verde
sphere_points = []
for a in np.linspace(0, 2 * np.pi, 500):
    # TODO: perguntar: pode ser assim né?
    for b in np.linspace(0, np.pi, 500):
        x, y, z = sphere(a, b)
        x, y = np.round(x).astype(int), np.round(y).astype(int)
        sphere_points.append((x, y, z))
sphere_points = list(set(sphere_points))
for x, y, z in sphere_points:
    zb.set_point(x, y, z, (0, 255, 0))

# Cubo branco
for x in range(-20, 21):
    for y in range(-20, 21):
        zb.set_point(x, y, -20, (255, 255, 255))
        zb.set_point(x, y, 20, (255, 255, 255))
        zb.set_point(x, 20, y, (255, 255, 255))
        zb.set_point(x, -20, y, (255, 255, 255))
        zb.set_point(20, x, y, (255, 255, 255))
        zb.set_point(-20, x, y, (255, 255, 255))

# purple
zb.set_point(10, 100, 5, (255, 0, 255))

zb.save('z-buffer.png')