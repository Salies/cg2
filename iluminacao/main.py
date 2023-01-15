from Illumination import Illumination

ilu = Illumination()
# self, Ia, Ka, Il, K, n
im = ilu.ilu_b(1.0, 0.5, 1.0, 6.0, 10.0)
im.show()