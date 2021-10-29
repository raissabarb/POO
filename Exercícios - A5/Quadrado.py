import random as rd


class Quadrado:

    def __init__(self, lado):
        self.face = lado

    def area(self):
        area = (self.face) * (self.face)
        return area

    def aumentar(self, novo):
        self.face = novo
        maior = 'A nova medida da face do quadrado é: {}'.format(self.face)
        return print(maior)


q1 = Quadrado(5)
print('A área é: {}'.format(q1.area()))
q1.aumentar(6)
print('A nova área é: {}\n'.format(q1.area()))

areas = []
soma_areas = 0
opc = int(input('Deseja ver as áreas dos quadrados aleatórios? [1 para sim, 0 para não] '))
if opc == 1:
    for i in range(0, 10):
        q = rd.randint(1, 10)
        quad = Quadrado(q)
        areas.append(quad.area())
        print('Área do quadrado {} é: {}'.format(i+1, quad.area()))
elif opc == 0:
    for i in range(0, 10):
        q = rd.randint(1, 10)
        quad = Quadrado(q)
        areas.append(quad.area())
soma_areas = sum(areas)
print('\nA soma das áreas dos 10 quadrados aleatórios é: {}'.format(soma_areas))