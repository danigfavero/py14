from banco import *

class ManipuladorDeTributaveis:

    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            if isinstance(t, Tributavel):
                total += t.get_valor_imposto()
            else:
                print(t.__repr__(), "não é um tributável")
        return total


if __name__ == "__main__":
    # cc1 = ContaCorrente('123-4', 'João', 1000.0)
    # cc2 = ContaCorrente('123-4', 'José', 1000.0)
    # seguro1 = SeguroDeVida(100.0, 'José', '345-77')
    # seguro2 = SeguroDeVida(200.0, 'Maria', '237-98')

    # lista_tributaveis = []
    # lista_tributaveis.append(cc1)
    # lista_tributaveis.append(cc2)
    # lista_tributaveis.append(seguro1)
    # lista_tributaveis.append(seguro2)

    # manipulador = ManipuladorDeTributaveis()
    # total = manipulador.calcula_impostos(lista_tributaveis)

    # print(total)

    cc = ContaCorrente('João', '123-4')
    cc.deposita(1000.0)

    seguro = SeguroDeVida(100.0, 'José', '345-77')

    ci = ContaInvestimento('Gildo', '123-0')
    ci.deposita(10.0)

    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroDeVida)
    Tributavel.register(ContaInvestimento)


    lista_tributaveis = []
    lista_tributaveis.append(cc)
    lista_tributaveis.append(seguro)
    lista_tributaveis.append(ci)

    mt = ManipuladorDeTributaveis()
    total = mt.calcula_impostos(lista_tributaveis)
    print(total)

    cp = ContaPoupanca('123-6', 'Maria')
    lista_tributaveis.append(cp)

    total = mt.calcula_impostos(lista_tributaveis)
    print(total)