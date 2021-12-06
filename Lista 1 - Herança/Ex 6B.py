import math


class Figura:
    def __init__(self, lado):
        self.lado = lado

    def __str__(self):
        return "Figura = %d" % self.lado

    def getArea(self):
        area = self.lado
        return area


class Circulo(Figura):
    def __init__(self, lado, raio):
        super(Circulo, self).__init__(lado)
        self.raio = raio

    def __str__(self):
        return "Circulo = (%d, %d)" % (self.lado, self.raio)

    def getArea(self):
        area = 3.14 * math.pow(self.raio, 2)
        return area


c = Circulo(0, 2)
areaC = c.getArea()
print(c)
print('Área do círculo: {}'.format(areaC))