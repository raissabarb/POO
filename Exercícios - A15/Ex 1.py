lista = []
cont = 0
num = -1

while cont < 100 and num != 0:
    num = int(input('Digite um número: '))
    lista.append(num)
    cont += 1

print(lista)
lista.sort()
print(lista)