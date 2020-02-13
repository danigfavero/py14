""" Exercícios 14.7 - Collections
"""
from collections.abc import MutableMapping


class Contas(MutableMapping):
    _dados = {}

    def __len__(self):
        return len(self._dados)

    def __getitem__(self, chave):
        return self._dados[chave]

    def __setitem__(self, chave, valor):
        if isinstance(valor, Conta):
            self._dados[chave] = valor
        else:
            raise ValueError("valor atribuido não é uma conta!")

    def __delitem__(self, chave):
        del self._dados[chave]

    def __iter__(self):
        return iter(self._dados)


if __name__ == "__main__":

    import csv
    from conta_excecoes import *

    contas = Contas()

    arquivo = open('contas.txt', 'r')
    leitor = csv.DictReader(arquivo)

    cnt = 1
    for linha in leitor:
        conta = ContaCorrente(linha["numero"], 
                              linha["titular"],
                              float(linha["saldo"]),
                              float(linha["limite"]))
        n = "conta" + str(cnt)
        contas[n] = conta
        cnt += 1

    arquivo.close()

    print('saldo \t\timposto \tatualizado')

    for c in contas.values():
        saldo = c.saldo
        imposto = c.get_valor_imposto()
        c.saca(imposto)
        print(f'{saldo} \t\t{imposto} \t\t{c.saldo}')