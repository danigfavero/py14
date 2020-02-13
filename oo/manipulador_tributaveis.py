""" Exercícios 12.6 - Interfaces e classes abstratas
"""
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
    from conta_interface import *
    from tributavel import Tributavel
   
    cc = ContaCorrente('João', '123-4')
    cc.deposita(1000.0)

    seguro = SeguroDeVida(100.0, 'José', '345-77')

    ci = ContaInvestimento('Ana', '123-0')
    ci.deposita(100.0)

    Tributavel.register(ContaCorrente)
    Tributavel.register(SeguroDeVida)
    Tributavel.register(ContaInvestimento)

    lista_tributaveis = [cc, seguro, ci]

    mt = ManipuladorDeTributaveis()
    total = mt.calcula_impostos(lista_tributaveis)
    print(total)

    cp = ContaPoupanca('123-6', 'Maria')
    lista_tributaveis.append(cp)

    total = mt.calcula_impostos(lista_tributaveis)
    print(total)
