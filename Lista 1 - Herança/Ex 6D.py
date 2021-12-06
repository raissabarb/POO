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


r = Retangulo(3, 4)
print('Área do retângulo: {}'.format(r.getArea()))
print(r)