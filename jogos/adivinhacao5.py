# Exercícios 7.11 - Refatoração
import random

def imprime_mensagem_abertura():
    print('***************************************')
    print('***Bem-vindx ao jogo da Adivinhação!***')
    print('***************************************')

def sorteia_numero_secreto():
    return random.randrange(0, 100)

def define_nivel():
    nivel = input('Escolha o nível 1, 2 ou 3:')
    if nivel == '1':
        tentativas = 20
    elif nivel == '2':
        tentativas = 10
    elif nivel == '3':
        tentativas = 5
    return tentativas

def imprime_tentativa(rodada, tentativas, pontos):
    print('Tentativa {} de {}'.format(rodada, tentativas))
    print('Você tem {} pontos'.format(pontos))

def chute_certo(chute, numero):
    acertou = (chute == numero)
    maior = (chute > numero)
    menor = (chute < numero)

    if acertou:
        print('Você acertou')
        return True
    elif maior:
        print('Você errou, seu chute foi maior que o número secreto')
    elif menor:
        print('Você errou, seu chute foi menor que o número secreto')

    pontos -= abs(numero - chute)
    return False

def imprime_fim_de_jogo(pontos):
    print("Fim de jogo.")
    print("Você fez {}/1000 pontos!".format(pontos))

def jogar():

    imprime_mensagem_abertura()
    numero = sorteia_numero_secreto()
    pontos = 1000
    tentativas = define_nivel()   

    for rodada in range(1, tentativas + 1):
        
        imprime_tentativa(rodada, tentativas, pontos)
        chute = int(input('Digite um número: '))

        if chute_certo(chute, numero):
            break

    imprime_fim_de_jogo(pontos)


if __name__ == "__main__":
    adivinhacao()