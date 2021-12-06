class Figura:
    def __init__(self):
        self.lado = 0

    def __str__(self):
        return "Figura = %d" % self.lado

    def getArea(self):
        area = self.lado
        return area


figX = Figura()
print(figX)
print(figX.getArea())