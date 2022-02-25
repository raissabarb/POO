class Funcionario:
    def __init__(self):
        self.sobrenome = ''
        self.nome = ''
        self.salarioHora = ''
        self.anosNaEmpresa = ''

    def get_nome(self, n):
        self.nome = n
        return self.nome

    def get_sobrenome(self, s):
        self.sobrenome = s
        return self.sobrenome

    def get_tempo(self, t):
        self.anosNaEmpresa = t
        return self.anosNaEmpresa

    def get_salario(self, s):
        self.salarioHora = s
        return self.salarioHora

    def infos(self, lista, anos):
        cont = 0
        print('-> Funcionários que se encaixam nas características da consulta:\n')
        for i in range(0, len(lista)):
            if lista_tempo_trabalhado[i] >= anos:
                cont += 1
                print('NOME: {} {}\nSALÁRIO: {}\n'.format(lista_nome_funcionarios[i], lista_sobrenome_funcionarios[i], lista_salarios[i]))
        if cont == 0:
            print('Nenhum funcionário encontrado!\n')


lista_nome_funcionarios = []
lista_sobrenome_funcionarios = []
lista_salarios = []
lista_tempo_trabalhado = []

p1 = Funcionario()
n1 = p1.get_nome('Raissa')
lista_nome_funcionarios.append(n1)
sn1 = p1.get_sobrenome('Barbosa')
lista_sobrenome_funcionarios.append(sn1)
s1 = p1.get_salario(500.00)
lista_salarios.append(s1)
t1 = p1.get_tempo(1)
lista_tempo_trabalhado.append(t1)

p2 = Funcionario()
n2 = p2.get_nome('Nádia')
lista_nome_funcionarios.append(n2)
sn2 = p2.get_sobrenome('Barbosa')
lista_sobrenome_funcionarios.append(sn2)
s2 = p2.get_salario(245.15)
lista_salarios.append(s2)
t2 = p2.get_tempo(2)
lista_tempo_trabalhado.append(t2)

p3 = Funcionario()
n3 = p3.get_nome('Pedro')
lista_nome_funcionarios.append(n3)
sn3 = p3.get_sobrenome('Souza')
lista_sobrenome_funcionarios.append(sn3)
s3 = p3.get_salario(1200.50)
lista_salarios.append(s3)
t3 = p3.get_tempo(2.5)
lista_tempo_trabalhado.append(t3)

tot_funcionarios = []
for i in range(0, 3):
    mix = lista_nome_funcionarios[i] + ' ' + lista_sobrenome_funcionarios[i]
    tot_funcionarios.append(mix)

# Estipulando um prazo de dois anos
p3.infos(lista_nome_funcionarios, 2)
print('\n')
# Estipulando um prazo de três anos
p3.infos(lista_nome_funcionarios, 3)
print('\n')
# Estipulando um prazo de um ano
p3.infos(lista_nome_funcionarios, 1)