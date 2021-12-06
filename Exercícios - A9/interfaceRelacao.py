import math


class interfaceRelacao:  # classe com o mesmo intuito da interface em Java
    def __init__(self):
        pass

    def maior_que(self, obj):
        pass

    def manor_que(self, obj):
        pass

    def igual_a(self, obj):
        pass


class Reta:
    def __init__(self, pontos, aux):
        self.x1 = pontos[0]
        self.x2 = pontos[2]
        self.y1 = pontos[1]
        self.y2 = pontos[3]
        self.auxiliar = aux

    def maior_que(self, obj):
        nx1 = int(obj[0])
        ny1 = int(obj[1])
        nx2 = int(obj[2])
        ny2 = int(obj[3])
        dist_nova = math.sqrt(math.pow((nx2 - nx1), 2) + math.pow((ny2 - ny1), 2))
        dist_original = math.sqrt(math.pow((self.x2 - self.x1), 2) + math.pow((self.y2 - self.y1), 2))
        if dist_nova > dist_original:
            result = 'True'
            self.auxiliar.append('+')
            return result
        else:
            result = 'False'
            self.auxiliar.append('+')
            return result

    def menor_que(self, obj):
        nx1 = int(obj[0])
        ny1 = int(obj[1])
        nx2 = int(obj[2])
        ny2 = int(obj[3])
        dist_nova = math.sqrt(math.pow((nx2 - nx1), 2) + math.pow((ny2 - ny1), 2))
        dist_original = math.sqrt(math.pow((self.x2 - self.x1), 2) + math.pow((self.y2 - self.y1), 2))
        if dist_nova < dist_original:
            result = 'True'
            self.auxiliar.append('-')
            return result
        else:
            result = 'False'
            self.auxiliar.append('-')
            return result

    def igual_a(self, obj):
        nx1 = int(obj[0])
        ny1 = int(obj[1])
        nx2 = int(obj[2])
        ny2 = int(obj[3])
        dist_nova = math.sqrt(math.pow((nx2 - nx1), 2) + math.pow((ny2 - ny1), 2))
        dist_original = math.sqrt(math.pow((self.x2 - self.x1), 2) + math.pow((self.y2 - self.y1), 2))
        if dist_nova == dist_original:
            result = 'True'
            self.auxiliar.append('=')
            return result
        else:
            result = 'False'
            self.auxiliar.append('=')
            return result


aux = []
pontos = [1, 2, 5, 2]
reta = Reta(pontos, aux)
novos_pontos = []
maiq = 0
menq = 0
ig = 0
for i in range(0, 4):
    num = input('Número {}: '.format(i+1))
    novos_pontos.append(num)
opc = int(input('\nDeseja fazer alguma comparação? [1 para sim, 0 para não] '))
while opc == 1:
    escolha = int(input('\n***** MENU *****\n1. Maior que\n2. Menor que\n3. Igual a\n'))
    if escolha == 1:
        maiq = reta.maior_que(novos_pontos)
        print('É maior? {}'.format(maiq))
        opc2 = int(input('\nDeseja fazer outra comparação? [1 para sim, 0 para não] '))
        if opc2 == 1:
            opc = 1
        else:
            opc = 0
    elif escolha == 2:
        menq = reta.menor_que(novos_pontos)
        print('É menor? {}'.format(menq))
        opc2 = int(input('\nDeseja fazer outra comparação? [1 para sim, 0 para não] '))
        if opc2 == 1:
            opc = 1
        else:
            opc = 0
    elif escolha == 3:
        ig = reta.igual_a(novos_pontos)
        print('É igual? {}'.format(ig))
        opc2 = int(input('\nDeseja fazer outra comparação? [1 para sim, 0 para não] '))
        if opc2 == 1:
            opc = 1
        else:
            opc = 0

if ('+' and '-' and '=') not in aux:
    raise NotImplementedError('There is at least one method missing!')