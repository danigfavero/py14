from conta import *


class AtualizadorDeContas:

    def __init__(self, selic, saldo_total=0):
        self._selic = selic
        self._saldo_total = saldo_total

    def roda(self, conta):
        if not hasattr(conta, 'atualiza'):
            print('instância de {} não implementa o método atualiza()'.format(self.__class__.__name__))
            return
        if not hasattr(conta, '_saldo'):
            print('instância de {} não implementa o atributo _saldo'.format(self.__class__.__name__))
            return
        print('Saldo anterior: {}'.format(self._saldo_total))
        self._saldo_total -= conta._saldo
        conta.atualiza(self._selic)
        self._saldo_total += conta._saldo
        print('Saldo final: {}'.format(self._saldo_total))


if __name__ == '__main__':
    c = Conta('123-4', 'Joao', 1000.0)
    cc = ContaCorrente('123-5', 'José', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)

    adc = AtualizadorDeContas(0.01)

    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)

    print('Saldo total: {}'.format(adc._saldo_total))
