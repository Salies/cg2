import numpy as np
from PIL import ImageQt
from ZBuffer import ZBuffer

# Função que recebe os pontos desenhados pelo usuário
# e retorna uma imagem com eles rotacionados com varredura.
def sweep(points):
    # Primeiramente tratamos os dados
    # Adiciona uma coluna de 0s para o z
    points = np.append(points, np.zeros((len(points), 1)), axis=1)
    # Adiciona uma coluna de 1s, pois a matriz de transformação precisa de coordenadas homogêneas
    points = np.append(points, np.ones((len(points), 1)), axis=1).astype(int)
    # Agora, subtrai a primeira coluna (x) de 200, e pega o abs
    points[:, 0] = abs(200 - points[:, 0])
    # Agora sim: podemos rotacionar
    # Preparando a matriz de rotação em x, apenas para uma melhor visualização
    deg = np.radians(30)
    Rx = np.array([
        [1, 0, 0, 0],
        [0, np.cos(deg), -np.sin(deg), 0],
        [0, np.sin(deg), np.cos(deg), 0],
        [0, 0, 0, 1]
    ])

    # Rotacionando cada ponto, e já desenhando no ZBuffer
    zb = ZBuffer((401, 400))
    # Aqui pulamos alguns pontos propositalmente para uma melhor visualização do objeto
    for i in range(0, len(points), 4):
        p = points[i]
        for g in np.linspace(0, 2 * np.pi, 360):
            T = np.array([
                [np.cos(g), 0, np.sin(g), 0],
                [0, 1, 0, 0],
                [-np.sin(g), 0, np.cos(g), 0],
                [0, 0, 0, 1]
            ])
            x, y, z, _ = p @ T @ Rx
            zb.set_point(x + 200, y, z, 0)

    return ImageQt.ImageQt(zb.to_img().convert('L'))