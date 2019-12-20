import abc
from historico import *
from tributavel import *

class Conta(abc.ABC):

    __slots__ = ['_numero', '_titular', '_saldo', '_historico']
    
    def __init__(self, numero, titular, saldo=0.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._historico = Historico()
        self._tipo = self.__class__.__name__

    def __str__(self):
        string = ('Conta: {} \tSaldo : {} \nTitular: {} {} \nCPF: {}'.format(
                 self._numero, self._saldo, self._titular.nome, 
                 self._titular.sobrenome, self._titular.cpf))
        string += '\nTransações:'
        for t in self._historico.transacoes:
            string += '\n- {}'.format(t)
        string += '\nTipo da Conta: {}'.format(self._tipo)
        return string
        

    @property
    def saldo(self):
        return self._saldo

    def deposita(self, valor):
        if valor < 0:
            raise ValueError('Você tentou depositar um valor negativo')
        else:
            self._saldo += valor
            self._historico.transacoes.append("depósito de {}".format(valor))

    def saca(self, valor):
        if valor < 0:
            raise ValueError('Você tentou depositar um valor negativo')
        if self._saldo < valor:
            raise SaldoInsuficienteError()
        self._saldo -= valor
        self._historico.transacoes.append("saque de {}".format(valor))

    def extrato(self):
        print("numero : {} \nsaldo: {}".format(self._numero, self._saldo))
        print("titular: {} {} \ncpf: {}".format(self._titular.nome, self._titular.sobrenome, self._titular.cpf))
        self._historico.transacoes.append("tirou extrato, saldo de {}".format(self._saldo))


    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou:
            destino.deposita(valor)
            self._historico.transacoes.append("transferência de {} para conta {}".format(valor, destino._numero))
        return retirou

    @abc.abstractmethod
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa


class ContaCorrente(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2

    def deposita(self, valor):
        super().deposita(valor)
        self._saldo -= 0.10

    def get_valor_imposto(self):
        return self._saldo * 0.01


class ContaPoupanca(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3


class ContaInvestimento(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5

    def get_valor_imposto(self):
        return self._saldo * 0.03

class SeguroDeVida():
    
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 42 + self._valor * 0.05


class SaldoInsuficienteError(RuntimeError):
    pass
    
if __name__ == '__main__':
    cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
    cliente2 = Cliente('José', 'Azevedo', '222222222-22')
    cliente3 = Cliente('Maria', 'Airam', '333333333-33')
    conta1 = ContaCorrente('123-4', cliente1, 1000.0)
    conta2 = ContaPoupanca('123-5', cliente2, 1000.0)
    conta3 = ContaInvestimento('123-6', cliente3, 1000.0)
    conta1.deposita(100.0)
    conta1.saca(50.0)
    conta1.transfere_para(conta2, 200.0)
    print(conta1)
    print(conta2)
    print(conta3)



