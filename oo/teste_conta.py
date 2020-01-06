"""teste conta
antes de aprender orientada a objetos
"""


def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    conta['saldo'] += valor


def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print("numero: {} \nsaldo: {}".format(conta['numero'], conta['saldo']))
