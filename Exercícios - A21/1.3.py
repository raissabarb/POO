class Shape:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width


class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class RasterBox(Coords):
    def __init__(self, x, y, topLeft, bottomRight):
        super().__init__(x, y)
        self.right = bottomRight
        self.left = topLeft

    def getTopLeft(self):
        return self.left

    def getBottomRight(self):
        return self.right


class Adaptor(RasterBox):
    def __init__(self, x, y, topLeft, bottomRight):
        super().__init__(x, y, topLeft, bottomRight)

    def returnX(self):
        return self.x

    def returnY(self):
        return self.y

    def returnTopLeft_height(self):
        return self.left

    def returnBottomRight_width(self):
        return self.right


class VectorDraw(Adaptor, Shape):
    pass


classe = VectorDraw(5, 10, 24.1, 30)
print(classe.x)
print(classe.right)
