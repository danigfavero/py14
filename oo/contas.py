""" Exercícios 14.7 - Collections
"""
from collections.abc import MutableSequence


class Contas(MutableSequence):
    _dados = []

    def __len__(self):
        return len(self._dados)

    def __getitem__(self, posicao):
        return self._dados[posicao]

    def __setitem__(self, posicao, valor):
        if isinstance(valor, Conta):
            self._dados[posicao] = valor
        else:
            raise ValueError("valor atribuido não é uma conta")

    def __delitem__(self, posicao):
        del self._dados[posicao]

    def insert(self, posicao, valor):
        if isinstance(valor, Conta):
            return self._dados.insert(posicao, valor)
        raise ValueError("valor atribuido não é uma conta")


if __name__ == "__main__":

    import csv
    from conta_excecoes import *

    contas = Contas()
    
    arquivo = open('contas.txt', 'r')
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        conta = ContaCorrente(linha["numero"], 
                              linha["titular"],
                              float(linha["saldo"]),
                              float(linha["limite"]))
        contas.append(conta)

    arquivo.close()

    print('saldo \t\timposto \tatualizado')

    for c in contas:
        saldo = c.saldo
        imposto = c.get_valor_imposto()
        c.saca(imposto)
        print(f'{saldo} \t\t{imposto} \t\t{c.saldo}')

