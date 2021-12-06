class interfaceCharSequence:  # classe com o mesmo intuito da interface em Java
    def __init__(self):
        pass

    def char_at(self, index):
        pass

    def length(self):
        pass

    def sub_sequence(self, start, end):
        pass

    def to_string(self):
        pass


class charSequence:
    def __init__(self, seq, aux):
        self.index = 0
        self.start = 0
        self.end = 0
        self.seq = seq
        self.auxiliar = aux

    def char_at(self, index):
        tam_lista = len(self.seq)
        for i in range(0, tam_lista):
            if i == index:
                caracter = self.seq[i]
                self.auxiliar.append('c')
                return caracter

    def length(self):
        tam_lista = len(self.seq)
        self.auxiliar.append('l')
        return tam_lista # obs

    def sub_sequence(self, start, end):
        nova_seq = self.seq
        tam_lista = len(self.seq)
        nova_seq[0] = start
        nova_seq[tam_lista-1] = end
        self.auxiliar.append('s')
        return nova_seq

    def to_string(self):
        juncao = "".join(str(_) for _ in self.seq)
        self.auxiliar.append('t')
        return juncao


lista_original = []
aux = []
tam_lista = int(input('Quantos caracteres deseja colocar na sua lista? '))
for i in range(0, tam_lista):
    caract = input('')
    lista_original.append(caract)
lista_original.reverse()
seq1 = charSequence(lista_original, aux)
opc = int(input('Vai utilizar sua lista? [1 para sim, 0 para não] '))
local1 = 0
tam1 = 0
subseq1 = ''
tipo_str1 = ''
while opc == 1:
    escolha = int(input('\n***** MENU *****\n1. Descobrir caractere\n2. Ver tamanho da lista\n3. Ver subsequência\n'
                        '4. Ver ''sequência no formato string\n'))
    if escolha == 1:
        indice1 = int(input('Digite um indice para descobrir o seu caractere: '))
        if indice1 > tam_lista:
            print('Erro!')
            indice1_1 = input('Digite outro indice para descobrir o seu caractere: ')
            local1 = seq1.char_at(indice1_1)
        else:
            local1 = seq1.char_at(indice1)
        opc2 = int(input('Vai utilizar sua lista novamente? [1 para sim, 0 para não] '))
        if opc2 == 1:
            opc = 1
        else:
            opc = 0
    elif escolha == 2:
        tam1 = seq1.length()
        opc2 = int(input('Vai utilizar sua lista novamente? [1 para sim, 0 para não] '))
        if opc2 == 1:
            opc = 1
        else:
            opc = 0
    elif escolha == 3:
        l1 = input('Digite um caractere: ')
        l2 = input('Digite outro caractere: ')
        subseq1 = seq1.sub_sequence(l1, l2)
        opc2 = int(input('Vai utilizar sua lista novamente? [1 para sim, 0 para não] '))
        if opc2 == 1:
            opc = 1
        else:
            opc = 0
    elif escolha == 4:
        tipo_str1 = seq1.to_string()
        opc2 = int(input('Vai utilizar sua lista novamente? [1 para sim, 0 para não] '))
        if opc2 == 1:
            opc = 1
        else:
            opc = 0
if ('c' and 'l' and 's' and 't') not in aux:
    raise NotImplementedError('There is at least one method missing!')
else:
    print('\n*** Resultados ***\n')
    print('Caractere do indice passado: {}'.format(local1))
    print('Tamanho da sua lista: {}'.format(tam1))
    print('Nova sequência: {}'.format(lista_original))
    print('Sequência no formato string: {}'.format(tipo_str1))