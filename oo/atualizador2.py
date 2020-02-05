"""Exercícios 11.7 - Herança e polimorfismo (opcionais)
"""
from conta_heranca import *


class AtualizadorDeContas:

    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    def roda(self, conta):
        # checando se a instância passada no argumento 'conta' é de uma
        # subclasse de "Conta":

        if isinstance(conta, Conta):

            print('Saldo anterior: {}'.format(self._saldo_total))

            self._saldo_total -= conta._saldo
            conta.atualiza(self._selic)

            self._saldo_total += conta._saldo

            print('Saldo final: {}'.format(self._saldo_total))

        else: # se não for do tipo 'Conta':

            print('Não foi possível rodar o atualizador de contas')


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

    # testando corner cases
    adc.roda(cliente1)
    adc.roda(3)
