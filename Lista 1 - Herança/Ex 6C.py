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


p = Paralelogramo(10, 6)
print('Área do paralelogramo: {}'.format(p.getArea()))
print(p)