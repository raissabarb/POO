from abc import ABC, abstractmethod


class RoboAbs(ABC):

    nome = ''
    posicaoXAtual = 0
    posicaoYAtual = 0
    direcao = 0

    def __init__(self):
        pass

    @abstractmethod
    def move(self, passos):
        pass


class RoboAbstrato(RoboAbs):
    def __init__(self, n, px, py, d):
        super(RoboAbstrato, self).__init__()
        self.nome = n
        self.posicaoXAtual = px
        self.posicaoYAtual = py
        self.direcao = d
        self.passos = 0

    def move(self, passos):
        self.passos = passos
        return self.passos

    def moveX(self, passos):
        self.posicaoXAtual += passos
        return self.posicaoXAtual

    def moveY(self, passos):
        self.posicaoYAtual += passos
        return self.posicaoYAtual

    def mudaDirecao(self, novaDir):
        self.direcao = novaDir
        return self.direcao

    def direcaoAtual(self):
        return self.direcao

    def toString(self):
        resultado = 'Nome do robô: {}\nPosição do robô: ({}, {})\nDireção do robô: {}'.format(self.nome, self.posicaoXAtual, self.posicaoYAtual, self.direcao)
        return resultado


class RoboSimples(RoboAbstrato):
    def __init__(self, n, px, py, d):
        super(RoboSimples, self).__init__(n, px, py, d)

    def move(self, passos):
        if self.direcaoAtual() == 0:
            self.moveX(passos)
        elif self.direcaoAtual() == 90:
            self.moveY(passos)
        elif self.direcaoAtual() == 180:
            self.moveX(-passos)
        elif self.direcaoAtual() == 270:
            self.moveY(-passos)


class RoboABateria(RoboAbstrato):
    def __init__(self, n, px, py, d, e):
        super(RoboABateria, self).__init__(n, px, py, d)
        self.energia = e
        self.energiaASerGasta = 0

    def move(self, passos):
        self.energiaASerGasta = passos * 10
        if self.energiaASerGasta <= self.energia:
            if self.direcaoAtual() == 0:
                self.moveX(passos)
            elif self.direcaoAtual() == 45:
                self.moveX(passos)
                self.moveY(passos)
            elif self.direcaoAtual() == 90:
                self.moveY(passos)
            elif self.direcaoAtual() == 135:
                self.moveX(passos)
                self.moveY(-passos)
            elif self.direcaoAtual() == 180:
                self.moveX(-passos)
            elif self.direcaoAtual() == 225:
                self.moveX(-passos)
                self.moveY(-passos)
            elif self.direcaoAtual() == 270:
                self.moveY(-passos)
            elif self.direcaoAtual() == 315:
                self.moveX(-passos)
                self.moveX(passos)
            self.energia -= self.energiaASerGasta

    def toString(self):
        resultado = super().toString() + '\nEnergia do robô: {}'.format(self.energia)
        return resultado

    def recarrega(self, energia):
        self.energia += energia
        return self.energia


r = RoboABateria('C3PO', 45, 45, 90, 100)
r.move(3)
print(r.direcaoAtual())
print(r.energia)
print(r.energiaASerGasta)
r.recarrega(10)
print(r.energia)
print(r.toString())