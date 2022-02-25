class Consulta:
    def __init__(self):
        pass

    def maior_num(self, vetor):
        maior = 0
        tam = len(vetor)
        for j in range(0, tam):
            if j == 0:
                maior = vetor[j]
            else:
                if vetor[j] >= maior:
                    maior = vetor[j]
        print(maior)


testando = Consulta()
vet = []
qtd = int(input('Quantos números quer colocar no vetor? '))
for i in range(0, qtd):
    num = int(input('Num: '))
    vet.append(num)
print(vet)
testando.maior_num(vet)
