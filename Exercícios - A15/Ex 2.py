vet_double = [2.1, 4.7, 12.56, 19.26, 4.75]

def media(vetor):
    tam_vetor = len(vetor)
    soma = 0
    for i in range(0, tam_vetor):
        soma += vetor[i]
    media = soma / tam_vetor
    return media

media_vet = media(vet_double)
print('Média dos valores do vetor passado: {:.2f}'.format(media_vet))
