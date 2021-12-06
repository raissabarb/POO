class Figura:
    def __init__(self, lado):
        self.lado = lado

    def __str__(self):
        return "Figura = %d" % self.lado

    def getArea(self):
        area = self.lado
        return area


class Paralelogramo(Figura):
    def __init__(self, lado, altura):
        super(Paralelogramo, self).__init__(lado)
        self.h = altura
        self.b = lado

    def __str__(self):
        return "Paralelogramo = (%d, %d)" % (self.b, self.h)

    def getArea(self):
        area = self.h * self.b
        return area


class Losango(Paralelogramo):
    def __init__(self, lado, altura):  # altura será a medida do lado maior do losango
        super(Losango, self).__init__(lado, altura)
        self.d = lado
        self.D = altura

    def __str__(self):
        return "Losango = (%d, %d)" % (self.d, self.D)

    def getArea(self):
        area = (self.d * self.D) / 2
        return area


l = Losango(10, 20)
print('Área do losango: {}'.format(l.getArea()))
print(l)