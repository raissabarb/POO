import math


class Figura:
    def __init__(self, lado):
        self.lado = lado

    def __str__(self):
        return "Figura = %d" % self.lado

    def getArea(self):
        area = self.lado
        return area


class Retangulo(Figura):
    def __init__(self, lado, lado2):
        super(Retangulo, self).__init__(lado)
        self.l1 = lado
        self.l2 = lado2

    def __str__(self):
        return "Retângulo = (%d, %d)" % (self.l1, self.l2)

    def getArea(self):
        area = self.l1 * self.l2
        return area


class Quadrado(Retangulo):
    def __init__(self, lado, lado2):
        super(Quadrado, self).__init__(lado, lado2)
        self.lado = lado
        self.lado2 = lado2

    def __str__(self):
        return "Quadrado = (%d, %d)" % (self.lado, self.lado2)

    def getArea(self):
        area = math.pow(self.lado, 2)
        return area


q = Quadrado(2, 2)
print('Área do quadrado: {}'.format(q.getArea()))
print(q)