# Exercício 6.9 - Utilizando funções para encapsulamento

def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')

    # inicializando variáveis úteis
    palavra_secreta = "BANANA"
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