import numpy as np
import matplotlib.pyplot as plt

def sweep():
    poligono =  [
                    [(16, 180, 0), (180, 180, 0)],
                    [(180, 86, 0), (180, 180, 0)],
                    [(120, 120, 0), (180, 86, 0)],
                    [(16, 36, 0), (120, 120, 0)],
                    [(16, 36, 0), (16, 180, 0)]
                ]

    poligono = np.array(poligono)

    # imprimindo a última dimensão
    print(poligono.shape)
    print(poligono)

    # plotando o poligono 3d
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(poligono[:,0,0], poligono[:,0,1], poligono[:,0,2], 'o-')
    ax.plot(poligono[:,1,0], poligono[:,1,1], poligono[:,1,2], 'o-')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # plt.show()

    # # rotacionando o poligono em seu próprio eixo z
    # def rotate_z(poligono, theta):
    #     rot = np.array([
    #         [np.cos(theta), -np.sin(theta), 0],
    #         [np.sin(theta), np.cos(theta), 0],
    #         [0, 0, 1]
    #     ])
    #     poligono_rot = np.zeros(poligono.shape)
    #     for i in range(poligono.shape[0]):
    #         for j in range(poligono.shape[1]):
    #             poligono_rot[i,j] = np.dot(rot, poligono[i,j])
    #     return poligono_rot

    # # rotacionando o poligono em seu próprio eixo'
    # poligono_rot = rotate_z(poligono, np.pi/2)

    # # plotando o poligono rotacionado
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot(poligono_rot[:,0,0], poligono_rot[:,0,1], poligono_rot[:,0,2], 'o-')
    # ax.plot(poligono_rot[:,1,0], poligono_rot[:,1,1], poligono_rot[:,1,2], 'o-')
    # ax.set_xlabel('X')
    # ax.set_ylabel('Y')
    # ax.set_zlabel('Z')
    # plt.show()

    # rotacionando o poligono em seu próprio eixo x
    def rotate_x(poligono, theta):
        rot = np.array([
            [1, 0, 0],
            [0, np.cos(theta), -np.sin(theta)],
            [0, np.sin(theta), np.cos(theta)]
        ])
        poligono_rot = np.zeros(poligono.shape)
        for i in range(poligono.shape[0]):
            for j in range(poligono.shape[1]):
                # cria nova matriz com os valores rotacionados
                poligono_rot[i,j] = np.dot(rot, poligono[i,j])
                

        return poligono_rot

    # rotacionando o poligono em seu próprio eixo x
    poligono_rot = rotate_x(poligono, np.pi/2)

    # plotando o poligono rotacionado
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(poligono_rot[:,0,0], poligono_rot[:,0,1], poligono_rot[:,0,2], 'o-')
    ax.plot(poligono_rot[:,1,0], poligono_rot[:,1,1], poligono_rot[:,1,2], 'o-')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # plt.show()

    # rotaciona o poligono em 360, e escreve uma matriz para cada rotação, e plota todas
    porra_toda = []
    for i in range(0, 360):
        poligono_rot = rotate_x(poligono, np.pi/180*i)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(poligono_rot[:,0,0], poligono_rot[:,0,1], poligono_rot[:,0,2], 'o-')
        ax.plot(poligono_rot[:,1,0], poligono_rot[:,1,1], poligono_rot[:,1,2], 'o-')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        porra_toda.append(poligono_rot)
        plt.close()

    return porra_toda

