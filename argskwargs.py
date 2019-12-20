def teste_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)

# ARG É POSICIONAL!
args = ('um', 2, 3)
teste_args_kwargs(*args)

# KWARG É POSICIONADO!
kwargs = {'arg3': 3, 'arg2': 'dois', 'arg1': 'um'}
teste_args_kwargs(**kwargs)

# NÃO FUNCIONA: como eu deveria consertar?
# Na declaração da função?
# args = (1, 2, 3, 4)
#teste_args_kwargs(*args)