import numpy as np
from ZBuffer import ZBuffer

# Função para retornar um ponto de uma esfera de raio 50
# centrada no ponto (0, 0, 0)
def sphere(a, b):
    return 50 * np.cos(a) * np.cos(b), 50 * np.sin(a) * np.cos(b), 50 * np.sin(b)

# Função para iluminar um ponto usando a iluminação ambiente e a componente difusa.
# Retorna a intensidade do ponto.
def ilu_d(Ia, Ka, Il, Kd, cos_theta):
    return Ia * Ka + Il * Kd * cos_theta

# Função para iluminar um ponto usando a iluminação ambiente, a componente difusa
# e a componente especular. Retorna a intensidade do ponto.
def ilu_ds(Ia, Ka, Il, d, K, Kd, cos_theta, Ks, cos_alpha, n):
    return Ia * Ka + (Il / (d + K)) * (Kd * cos_theta + Ks * cos_alpha ** n)

# Classe para definir os objetos e iluminá-los
class Illumination:
    def __init__(self):
        self.sphere_points = np.empty((395641, 3))
        self.plane_points = np.empty((10000, 3), dtype=int)

        i = 0
        # Gerando os pontos da esfera
        for a in np.arange(0, 2 * np.pi, 0.01):
            for b in np.arange(0, 2 * np.pi, 0.01):
                self.sphere_points[i] = sphere(a, b)
                i += 1

        i = 0
        # Gerando os pontos do plano. Trata-se de um quadrado de lado 100
        # com centro em (50, 50, 0), ou seja, partindo de (0, 0, 0).
        for x in range(100):
            for y in range(100):
                self.plane_points[i] = (x, y, 0)
                i += 1

        # Os pontos x e y da esfera precisam ser arredondados para poderem
        # ser usados como índices.
        self.sphere_points[:, :2] = np.round(self.sphere_points[:, :2])

        # Outros valores necessários
        self.light = (100, 0, 100)
        observer = (0, 0, 100)
        self.sphere_color = np.array([255, 0, 255])
        self.plane_color = np.array([0, 0, 255])
        
        # O alpha é sempre o mesmo porque o observador está sempre na mesma posição
        cos_alpha = np.dot(observer, self.light) / (np.linalg.norm(observer) * np.linalg.norm(self.light))
        self.alpha = np.arccos(cos_alpha)

    def _get_cos(self, normal):
        return np.dot(normal, self.light) / (np.linalg.norm(normal) * np.linalg.norm(self.light))

    # Devolve uma imagem iluminada (ambiente e difusa)
    def ilu_a(self, Ia, Ka, Il, Kd_shpere, Kd_plane):
        zb = ZBuffer((300, 300), 150)
        for p in self.sphere_points:
            # Calcula a normal da esfera no ponto (é o próprio ponto)
            normal = p
            # Calcula o cosseno do ângulo entre a normal e a luz
            cos_theta = self._get_cos(normal)
            # Calcula a intensidade do ponto
            i = ilu_d(Ia, Ka, Il, Kd_shpere, cos_theta)
            # Ajusta a cor do ponto
            c = self.sphere_color * i
            # Desenha o ponto
            zb.set_point(*p, c)

        for p in self.plane_points:
            x, y, _ = p
            # Calcula a normal do plano
            normal = np.array([x, y, 1])
            # Calcula o cosseno do ângulo entre a normal e a luz
            cos_theta = self._get_cos(normal)
            # Calcula a intensidade do ponto
            i = ilu_d(Ia, Ka, Il, Kd_plane, cos_theta)
            # Ajusta a cor do ponto
            c = self.plane_color * i
            # Desenha o ponto
            zb.set_point(*p, c)

        return zb.to_img()

    # Iluminação ambiente, difusa e especular
    def ilu_b(self, Ia, Ka, Il, K, n, Kd_sphere, Kd_plane, Ks_sphere, Ks_plane):
        zb = ZBuffer((300, 300), 150)
        for p in self.sphere_points:
            normal = p
            cos_theta = self._get_cos(normal)
            cos_alpha = np.cos(self.alpha - 2 * np.arccos(cos_theta))
            d = np.linalg.norm(p - self.light)
            i = ilu_ds(Ia, Ka, Il, d, K, Kd_sphere, cos_theta, Ks_sphere, cos_alpha, n)
            c = self.sphere_color * i
            zb.set_point(*p, c)

        for p in self.plane_points:
            x, y, _ = p
            normal = np.array([x, y, 1])
            cos_theta = self._get_cos(normal)
            cos_alpha = np.cos(self.alpha - 2 * np.arccos(cos_theta))
            d = np.linalg.norm(p - self.light)
            i = ilu_ds(Ia, Ka, Il, d, K, Kd_plane, cos_theta, Ks_plane, cos_alpha, n)
            c = self.plane_color * i
            zb.set_point(*p, c)

        return zb.to_img()
            
    # Devolve uma imagem sem iluminação
    def no_ilu(self):
        zb = ZBuffer((300, 300), 150)
        for p in self.sphere_points:
            zb.set_point(*p, self.sphere_color)

        for p in self.plane_points:
            zb.set_point(*p, self.plane_color)

        return zb.to_img()