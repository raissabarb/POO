class Triangulo:

    def __init__(self, base, altura):
        if base == 0 and altura == 0:
            self.b = 5
            self.h = 4
        else:
            self.b = base
            self.h = altura

    def setBase(self, base):
        self.b = base
        return self.b

    def setAltura(self, altura):
        self.h = altura
        return self.h

    def getBase(self):
        return self.b

    def getAltura(self):
        return self.h

    def area(self):
        area = (self.b*self.h)/2
        return print('A área do triângulo descrito é: {}\n'.format(area))

    def mostra(self):
        return print('Base: {}\nAltura: {}\n'.format(self.b, self.h))


escolha = int(input('Deseja digitar as medidas ou não? [1 para sim, 0 para não] '))
if escolha == 1:
    base1 = input('Digite um valor para a base do triângulo: ')
    altura1 = input('Agora, um para a altura: ')
    t1 = Triangulo(int(base1), int(altura1))
    t1.mostra()
    t1.area()
    base2 = input('Digite um valor para a base do triângulo: ')
    altura2 = input('Agora, um para a altura: ')
    t2 = Triangulo(int(base2), int(altura2))
    t2.area()
    t2.setAltura(3)
    t2.area()

elif escolha == 0:
    base3, altura3 = 0, 0
    t3 = Triangulo(int(base3), int(altura3))
    t3.mostra()
    novaB = t3.setBase(7)
    print('Nova base: {}'.format(novaB))
    altura = t3.getAltura()
    print('Base: {}'.format(novaB))
    print('Altura: {}'.format(altura))