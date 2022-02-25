import math as mt

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def perimetro_quadrado(self):
        perim1 = self.lado * 4
        return perim1

    def area_quadrado(self):
        area1 = self.lado * self.lado
        return area1


class Triangulo:
    def __init__(self, l1, l2, l3):
        self.lado1 = l1
        self.lado2 = l2
        self.lado3 = l3

    def perimetro_triangulo(self):
        perim2 = self.lado1 + self.lado2 + self.lado3
        return perim2

    def area_triangulo(self):
        p = (self.lado1 + self.lado2 + self.lado3) / 2
        area2 = mt.sqrt(p * (p - self.lado1) * (p - self.lado2) * (p - self.lado3))
        return area2

    def tipo_triangulo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            return print('Triângulo EQUILÁTERO')
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado2 != self.lado3:
            return print('Triângulo ESCALENO')
        elif (self.lado1 == self.lado2 and self.lado1 != self.lado3) or (self.lado2 == self.lado3 and self.lado2 != self.lado1) or (self.lado1 == self.lado3 and self.lado2 != self.lado1):
            return print('Triângulo ISÓSCELES')


esc_obj = int(input('Deseja criar um objeto? [1 para sim, 0 para não] '))
if esc_obj == 1:
    while esc_obj == 1:
        print('\n ------------------- MENU --------------------')
        print(' Escolha uma opção:')
        print(' 1 - Quadrado\n 2 - Triângulo\n ---------------------------------------------')
        opc = int(input(' '))
        if opc == 1:
            lado = float(input('Qual será a medida dos lados do quadrado? '))
            q = Quadrado(lado)
            print('\n* O perímetro do quadrado criado é: {:.2f}'.format(q.perimetro_quadrado()))
            print('* A área do quadrado é: {:.2f}'. format(q.area_quadrado()))
            escolha2 = int(input('\nDeseja criar outro objeto? [1 para sim, 0 para não] '))
            if escolha2 == 1:
                esc_obj = 1
            else:
                esc_obj = 0
        elif opc == 2:
            l1 = float(input('Qual será a medida do lado 1 do triângulo? '))
            l2 = float(input('Qual será a medida do lado 2 do triângulo? '))
            l3 = float(input('Qual será a medida do lado 3 do triângulo? '))
            if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
                t = Triangulo(l1, l2, l3)
                print('\n* O perímetro do triângulo criado é: {:.2f}'. format(t.perimetro_triangulo()))
                print('* A área do triângulo é: {:.2f}'.format(t.area_triangulo()))
                print('\n* Tipo:')
                t.tipo_triangulo()
                escolha3 = int(input('\nDeseja criar outro objeto? [1 para sim, 0 para não] '))
                if escolha3 == 1:
                    esc_obj = 1
                else:
                    esc_obj = 0
            else:
                print('\nERRO! Números não compatíveis com um triângulo!')
                escolha4 = int(input('\nDeseja fazer outra tentativa? [1 para sim, 0 para não] '))
                if escolha4 == 1:
                    esc_obj = 1
                else:
                    esc_obj = 0
        else:
            print('\nERRO! Número não reconhecido!')
            escolha5 = int(input('\nDeseja fazer outra tentativa? [1 para sim, 0 para não] '))
            if escolha5 == 1:
                esc_obj = 1
            else:
                esc_obj = 0
if esc_obj == 0:
    print('Finalizando...')
if (esc_obj != 1) and (esc_obj != 0):
    print('\nERRO! Caractere não reconhecido!')
    print('Finalizando...')