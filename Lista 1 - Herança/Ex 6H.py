class Figura:
    def __init__(self, lado):
        self.lado = lado

    def __str__(self):
        return "Figura = %d" % self.lado

    def getArea(self):
        area = self.lado
        return area


class Triangulo(Figura):
    def __init__(self, lado, altura):
        super(Triangulo, self).__init__(lado)
        self.b = lado
        self.h = altura

    def __str__(self):
        return "Triângulo = (%d, %d)" % (self.b, self.h)

    def getArea(self):
        area = (self.b * self.h) / 2
        return area


class TrianguloRetangulo(Triangulo):
    def __init__(self, lado, altura, lado3):
        super(TrianguloRetangulo, self).__init__(lado, altura)
        self.a = lado
        self.b = altura
        self.c = lado3

    def __str__(self):
        return "TrianguloRetangulo = (%d, %d, %d)" % (self.a, self.b, self.c)

    def getArea(self):
        area = (self.b * self.c) / 2
        return area


tr = TrianguloRetangulo(5, 4, 3)
print('Área do triângulo retângulo: {}'.format(tr.getArea()))
print(tr)