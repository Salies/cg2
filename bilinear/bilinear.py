import numpy as np

# Essa função recebe os quatro pontos do plano e retorna
# os pontos que farão a composição deste plano na imagem,
# de acordo com a modelagem via superfície bilinear.
def bilinear(p00, p01, p10, p11):
    points = []
    for u in np.arange(0, 1, 0.01):
        for v in np.arange(0, 1, 0.01):
            p = p00 * (1 - u) * (1 - v) + p01 * (1 - u) * v + p10 * u * (1 - v) + p11 * u * v
            points.append(p)
    # Como x e y precisam ser inteiros para serem usados como índices,
    # arrendodamos seus valores e retiramos os pontos duplicados.
    points = np.array(points)
    # Arredonda apenas os valores de x e y
    points[:, 0] = np.round(points[:, 0])
    points[:, 1] = np.round(points[:, 1])
    # Remove duplicados
    points = np.unique(points, axis=0)
    return points

ret_test = [
    (0, 0, 0),
    (20, 0, 0),
    (0, 20, 0),
    (20, 20, 0)
]

ret_test2 = [
    [20, 0, 80],
    [20, 40, 80],
    [100, 0, 0],
    [100, 40, 0]
]

ret_test = np.array(ret_test2)

print(bilinear(ret_test[0], ret_test[1], ret_test[2], ret_test[3]))