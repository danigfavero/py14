from atualizador import *


class Banco:

    def __init__(self, contas=[], total=0):
        self._contas = contas
        self._total_de_contas = total

    def adiciona(self, conta):
        self._contas.append(conta)
        self._total_de_contas += 1

    def pegaConta(self, pos):
        return self._contas[pos]

    def pegaTotalDeContas(self):
        return self._total_de_contas


if __name__ == '__main__':
    cc = ContaCorrente('123-5', 'José', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)
    b = Banco()
    b.adiciona(cc)
    b.adiciona(cp)
    adc = AtualizadorDeContas(0.01)
    for i in range(b.pegaTotalDeContas()):
        adc.roda(b.pegaConta(i))
