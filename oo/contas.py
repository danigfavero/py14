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
    from conta import ContaCorrente, Conta

    contas = Contas()
    
    arquivo = open('contas.txt', 'r')
    leitor = csv.reader(arquivo)

    for linha in leitor:
        conta = ContaCorrente(linha[0], linha[1], float(linha[2]))
        contas.append(conta)

    arquivo.close()

    print('saldo \timposto \tatualizado')

    for c in contas:
        saldo = c.saldo
        imposto = c.get_valor_imposto()
        c.saca(imposto)
        print('{} \t{} \t{}'.format(saldo, imposto, c.saldo))
