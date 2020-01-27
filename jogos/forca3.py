# Exercício 7.8 - Leitura de arquivos

import random # importando a biblioteca que gera números aleatórios


def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')


    # inicializando palavra secreta
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        # construindo lista de palavras a partir do arquivo
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    # sorteia um índice para escolher a palavra aleatoriamente
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper() 
    letras_acertadas = ['_' for letra in palavra_secreta]


    # inicializando variáveis
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    acertou = False
    enforcou = False
    erros = 0

    # jogando...
    while not acertou and not enforcou:

        print(letras_acertadas)
        # pede chute
        chute = input('Qual letra? ')
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            # marca chute
            posicao = 0
            for letra in palavra:
                if chute.upper() == letra.upper():
                    letras_acertadas[posicao] = letra
                posicao += 1
        
        else:
            # marca erro
            erros +=1  

        # atualiza booleanos
        acertou = '_' not in letras_acertadas
        enforcou = (erros == 7)

    print('Fim do jogo')


if __name__ == "__main__":
    # só é executado quando rodamos este módulo.
    # se importarmos esse módulo em outro lugar, esse trecho é ignorado.
    jogar()