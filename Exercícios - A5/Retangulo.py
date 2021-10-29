class Retangulo:

    def __init__(self, base, altura):
        self.b = base
        self.h = altura

    def area(self):
        area = self.b * self.h
        print_a = 'A área do retângulo especificado é: {}'.format(area)
        return print(print_a)

    def perimetro(self):
        perimetro = (2 * self.b) + (2 * self.h)
        print_p = 'O perímetro é: {}'.format(perimetro)
        return print(print_p)

    def relacao(self):
        r = self.b / self.h
        print_r = 'Relação entre base e altura: {}'.format(r)
        return print(print_r)

    def e_quadrado(self):
        if self.b == self.h:
            return print('O retângulo é, também, um quadrado!')
        else:
            return print('O retângulo não é um quadrado!')

    def imprime_info(self):
        info = '\n* Dimensões *\nBase: {}\nAltura: {}\n'.format(self.b, self.h)
        return print(info)


ret1 = Retangulo(3, 4)
ret1.imprime_info()
ret1.area()
ret1.perimetro()
ret1.relacao()
ret1.e_quadrado()

ret2 = Retangulo(5, 5)
ret2.imprime_info()
ret2.perimetro()
ret2.e_quadrado()