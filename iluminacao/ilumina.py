import numpy as np
from PIL import Image
from ZBuffer import ZBuffer

# Função para retornar um ponto de uma esfera de raio 50
# centrada no ponto (0, 0, 0)
def sphere(a, b):
    return 50 * np.cos(a) * np.cos(b), 50 * np.sin(a) * np.cos(b), 50 * np.sin(b)

# Função para iluminar um ponto usando a iluminação ambiente e a componente difusa
def ilu_d(Ia, Ka, Il, Kd, theta):
    return Ia * Ka + Il * Kd * np.cos(theta)

sphere_points = np.empty((395641, 3))
plane_points = np.empty((10000, 3))

i = 0
# Gerando os pontos da esfera
for a in np.arange(0, 2 * np.pi, 0.01):
    for b in np.arange(0, 2 * np.pi, 0.01):
        sphere_points[i] = sphere(a, b)
        i += 1        

i = 0
# Gerando os pontos do plano. Trata-se de um quadrado de lado 100
# com centro em (50, 50, 0), ou seja, partindo de (0, 0, 0).
for x in range(100):
    for y in range(100):
        plane_points[i] = (x, y, 0)
        i += 1

sphere_points = np.array(sphere_points)
# Os pontos x e y da esfera precisam ser arredondados para poderem
# ser usados como índices.
sphere_points[:, :2] = np.round(sphere_points[:, :2])
# Os pontos do plano podem ser inteiros de uma vez porque o z nunca muda (sempre 0).
plane_points = np.array(plane_points, dtype=int)

zb = ZBuffer((300, 300), 150)

for p in sphere_points:
    # A esfera é magenta
    zb.set_point(*p, (255, 0, 255))

for p in plane_points:
    # O plano é azul
    zb.set_point(*p, (0, 0, 255))

zb.to_img().show()