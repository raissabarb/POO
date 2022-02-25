from random import uniform


class CriaVetor:
    def __init__(self, tam):
        self.tam = tam

    def cria(self):
        vetor = []
        for i in range(self.tam):
            num = uniform(1, 50)
            vetor.append(num)
        return vetor


tam = int(input('Quantos números terá o vetor? '))
novo = CriaVetor(tam)
novovet = novo.cria()
for i in range(tam-1):
    print('{:.2f} - '.format(novovet[i]), end="")
print('{:.2f}'.format(novovet[tam-1]), end="")
