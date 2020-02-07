''' Validador de cpf, conforme as normas do ministério da fazenda
'''

def eh_inteiro(caracter):
    ''' Recebe um caracter e verifica se é possível transformá-lo em inteiro.
    Devolve True caso seja possível e False caso contrário.
    '''
    try: 
        int(caracter)
        return True
    except ValueError:
        return False


def arruma_formato(entrada):
    ''' Recebe um iterável contendo um cpf.
    Devolve uma lista com todos os inteiros encontrados no iterável, na ordem
    em que foram inseridos no iterável.
    '''
    digitos = []
    for digito in entrada:
        if eh_inteiro(digito):
            digitos.append(eval(digito))
    return digitos


def verifica_tamanho(digitos):
    ''' Recebe uma lista contendo um cpf e checa se há 11 dígitos.
    '''
    return len(digitos) == 11
        
    
def verifica_repetidos(digitos):
    ''' Checa se o cpf é do formato '111.111.111-11'.
    Devolve True se for um cpf válido e False caso contrário.
    '''
    return digitos.count(digitos[0]) < 11


def verificacao1(digitos):
    ''' Faz a primeira verificação pedida pelo ministério da fazenda.
    Devolve True se for um cpf válido e False caso contrário.
    '''
    digitos_iniciais = digitos[:9]
    digito_verificador = digitos[9]

    soma = 0
    for i in range(9):
        soma += digitos_iniciais[i] * (10-i)

    resto = ((soma*10) % 11) % 10
    return resto == digito_verificador


def verificacao2(digitos):
    ''' Faz a segunda verificação pedida pelo ministério da fazenda.
    Devolve True se for um cpf válido e False caso contrário.
    '''
    digitos_iniciais = digitos[:10]
    digito_final = digitos[10]

    soma = 0
    for i in range(10):
        soma += digitos_iniciais[i] * (11-i)

    resto = ((soma*10) % 11) % 10
    return resto == digito_final


def verifica_cpf(cpf):
    ''' Recebe um iterável contendo um cpf.
    Devolve True se for um cpf válido e False caso contrário.
    '''
    digitos = arruma_formato(cpf)
    return verifica_tamanho(digitos) and verifica_repetidos(digitos) and \
            verificacao1(digitos) and verificacao2(digitos)


if __name__ == "__main__":

    entrada = input("Digite seu cpf: ")

    if verifica_cpf(entrada):
        print("cpf válido!")
    else:
        print("cpf inválido!")

