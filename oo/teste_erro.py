from conta import ContaCorrente


def metodo1():
    print('início do método1')
    metodo2()
    print('fim do metodo1')


def metodo2():
    print('início do metodo2')
    cc = ContaCorrente('José', '123')
    for i in range(1, 15):
        cc.deposita(i + 1000)
        print(cc.saldo)
        if i == 5:
            cc = None
    print('fim do metodo2')


if __name__ == "__main__":
    print('início do main')
    try:
        metodo1()
    except AttributeError:
        print('errou')
    print('fim da main')
