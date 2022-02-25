class Analise:
    def __init__(self, arq_origem, arq_final):
        self.arq1 = arq_origem
        self.arq2 = arq_final

    def analisa(self):
        aberto1 = open('{}'.format(self.arq1), 'r')
        aberto2 = open('{}'.format(self.arq2), 'w')
        qtd_letras = 0
        qtd_vogais = 0
        qtd_consoantes = 0
        qtd_num = 0
        qtd_outros_caract = 0
        with aberto1 as file:
            for line in file:
                for letter in line:
                    qtd_letras += 1
                    if chr(65) <= letter <= chr(90) or chr(97) <= letter <= chr(122):
                        if letter == 'a' or letter == 'A' or letter == 'e' or letter == 'E' or letter == 'i' or letter == 'I' or\
                                letter == 'o' or letter == 'O' or letter == 'u' or letter == 'U':
                            qtd_vogais += 1
                        else:
                            qtd_consoantes += 1
                    elif letter == '1' or letter == '2' or letter == '3' or letter == '4' or letter == '5' or letter == '6' or \
                            letter == '7' or letter == '8' or letter == '9' or letter == '0':
                        qtd_num += 1
                    else:
                        qtd_outros_caract += 1
        aberto1.close()
        aberto2.write('Letras totais: {}\nConsoantes: {}\nVogais: {}\nNúmeros: {}\nOutros caracteres: {}'
                      .format(qtd_letras, qtd_consoantes, qtd_vogais, qtd_num, qtd_outros_caract))
        aberto2.close()


verifica = 'verifica.txt'
resultado = 'resultado.txt'
analise1 = Analise(verifica, resultado)
analise1.analisa()
abre = open('{}'.format(resultado), 'r')
with abre as arq:
    for line in arq:
        print(line)
