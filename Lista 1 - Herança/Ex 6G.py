class Figura:
    def __init__(self, lado):
        self.lado = lado

    def __str__(self):
        return "Figura = %d" % self.lado

    def getArea(self):
        area = self.lado
        return area


class Triangulo(Figura):  # precisa das condições de triangulo?
    def __init__(self, lado, altura):
        super(Triangulo, self).__init__(lado)
        self.b = lado
        self.h = altura

    def __str__(self):
        return "Triângulo = (%d, %d)" % (self.b, self.h)

    def getArea(self):
        area = (self.b * self.h) / 2
        return area


t = Triangulo(3, 5)
print('Área do triângulo: {}'.format(t.getArea()))
print(t)