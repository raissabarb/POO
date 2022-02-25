arquivo = input('Qual é o arquivo que será analisado? ')
caractere = input('Qual caractere deseja contabilizar no arquivo dado? ')
cont = 0
arq = open("{}".format(arquivo), "r")
with arq as a:
    for palavra in a:
        for letra in palavra:
            if letra == caractere or letra == caractere.upper():
                cont += 1
print('Caractere "{}" encontrado {} vezes!'.format(caractere, cont))
arq.close()
