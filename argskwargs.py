# 6.8 Exercícios - args e kwargs 

def teste_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)

args = ('um', 2, 3)
teste_args_kwargs(*args)

kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um'}
teste_args_kwargs(**kwargs)


# Não é possível chamar a mesma função com um quarto argumento na variável
# args e kwargs dos exercícios anteriores. Isso ocorre porque nossa definição
# da função teste_args_kwargs() recebe apenas 3 argumentos.


# Podemos resolver esse problema na definição da função, utilizando *args e
# permitindo que o usuário chame a função com quantos argumentos quiser
def teste_args_kwargs(*args):
    contador = 1 # como não sabemos quantos args teremos, precisamos contar
    for arg in args:
        print(f"arg{contador}: {arg}")
        contador += 1
