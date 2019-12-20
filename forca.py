import random

def imprime_mensagem_abertura():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')


def carrega_palavra():
    palavras = []
    
    arquivo = open('palavras.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]

def pede_chute():
    chute = input('Qual letra? ')
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra, chute, letras_acertadas):
    posicao = 0
    for letra in palavra: # iteradores :-D
        if chute.upper() == letra.upper():
            letras_acertadas[posicao] = letra
        posicao += 1


def imprime_mensagem_vencedor():
    print('Parabéns, você ganhou!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra):
    print('Puxa, você foi enforcado!')
    print('A palavra era {}'.format(palavra))
    print("    _______________         ")
    print("   /               \        ")
    print("  /                 \       ")
    print("//                   \/\    ")
    print("\|   XXXX     XXXX   | /    ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/      ")
    print("   |\     XXX     /|        ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/        ")
    print("     \_         _/          ")
    print("       \_______/            ")

def desenha_forca(erros):
    pass

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    
    print(letras_acertadas)

    acertou = False
    enforcou = False
    erros = 0

    while not acertou and not enforcou:
        chute = pede_chute()

        if chute in palavra_secreta:
           marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros +=1  
            desenha_forca(erros)

        print(letras_acertadas)

        acertou = '_' not in letras_acertadas
        enforcou = erros == 7

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print('Fim do jogo')