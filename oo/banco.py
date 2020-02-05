"""Exercícios 11.7 - Herança e polimorfismo (opcionais)
"""
from atualizador import *


class Banco:

    def __init__(self, contas=[], total=0):
        self._contas = contas
        self._total_de_contas = total

    def adiciona(self, conta):
        """ Adiciona uma conta na lista de contas
        """
        self._contas.append(conta)
        self._total_de_contas += 1

    def pega_conta(self, posicao):
        """ Devolve a conta em determinada posição da lista
        """
        return self._contas[posicao]

    def pega_total_de_contas(self):
        """ Retorna o total de contas na lista
        """
        return self._total_de_contas


if __name__ == '__main__':

    # teste: criando várias contas...
    cc = ContaCorrente('123-5', 'José', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0)

    # inserindo no banco
    meu_banco = Banco()
    meu_banco.adiciona(cc)
    meu_banco.adiciona(cp)

    # atualizando todas as contas do meu banco
    adc = AtualizadorDeContas(0.01)
    for conta in range(meu_banco.pega_total_de_contas()):
        adc.roda(meu_banco.pega_conta(conta)
