""" Exercícios 13.7 - Exceções (desafio)
"""
from conta_excecoes import *

class CaixaEletronico:

    def saque(self, conta, valor):
        try:
            conta.saca(valor)
            print(f'Saque de {valor} realizado com sucesso')
        except ValueError:
            print('O valor a ser sacado deve ser um número positivo.')
        except SaldoInsuficienteError:
            print('Você não possui saldo suficiente para concluir esta operação.')
    
    def deposito(self, conta, valor):
        try:
            conta.deposita(valor)
            print(f'Depósito de {valor} realizado com sucesso.')
        except ValueError:
            print('O valor a ser depositado deve ser um número positivo.')

if __name__ == "__main__":
    caixa = CaixaEletronico()
    cc = ContaCorrente('123-4', 'João', 1000.0)
    cp = ContaPoupanca('123-5', 'José', 800.0)
    
    caixa.saque(cc, 5000)
    caixa.saque(cp, -1000)
    caixa.deposito(cc, -10)