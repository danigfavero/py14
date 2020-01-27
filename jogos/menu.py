# Exercícios 6.9 - Módulos e encapsulamento

# importa o código dos respectivos módulos citados
import adivinhacao4 as adivinhacao # esse "as" é como eu vou chamar o módulo
import forca2 as forca

print('*********************************')
print('**********MENU DE JOGOS**********')
print('*********************************')
print("1. Adivinhação")
print("2. Forca")
escolha = int(input("Qual jogo quer jogar? Digite o número: "))

# inicializa algum dos dois jogos
if escolha == 1:
    adivinhacao.jogar() # <nome_do_modulo>.<funcao_no_modulo>()
elif escolha == 2:
    forca.jogar()
