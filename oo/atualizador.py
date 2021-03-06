"""Exercícios 11.7 - Herança e polimorfismo
"""
from conta_heranca import *


class AtualizadorDeContas:

    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    def roda(self, conta):
        # imprime o saldo anterior:
        print('Saldo anterior: {}'.format(self._saldo_total))

        # atualiza a conta:
        self._saldo_total -= conta._saldo
        conta.atualiza(self._selic)

        # soma o saldo final ao atributo _saldo_total
        self._saldo_total += conta._saldo

        # imprime o saldo final
        print('Saldo final: {}'.format(self._saldo_total))


if __name__ == '__main__':

    cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
    cliente2 = Cliente('José', 'Azevedo', '222222222-22')
    cliente3 = Cliente('Maria', 'Costa', '333333333-33')

    c = Conta('123-4', cliente1, 1000.0)
    cc = ContaCorrente('123-5', cliente2, 1000.0)
    cp = ContaPoupanca('123-6', cliente3, 1000.0)

    adc = AtualizadorDeContas(0.01)

    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)

    print('Saldo total: {}'.format(adc._saldo_total))


# Note que a classe AtualizadorDeContas não depende do método 'atualiza()'
# particular de cada classe filha de 'Conta'.
