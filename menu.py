from adivinhacao3 import adivinhacao
from forca import jogar as forca


print("****JOGOS****")
print("1. Adivinhação")
print("2. Forca")
escolha = int(input("Qual jogo quer jogar? Digite o número: "))

while True:
    if escolha == 1:
        adivinhacao()
        break
    elif escolha == 2:
        forca()
        break
    else:
        escolha = int(input("Qual jogo quer jogar? Digite o número: "))



