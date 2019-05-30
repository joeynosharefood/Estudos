def fatorial(x, show=False):
    """
    Param x = Recebe o valor escolhido para o fatorial
    Param show = Seu padrão sendo falso, para nao mostrar o calculo de 
    fatorial, porem se escolhido True, ele demonstra calculo por calculo utilizado 
    para chegar no valor final

    By JoeyNoShareFood
    """
    f = 1
    if show == True:
        for c in range(x, 0, -1):
            print(f'{c}x', end='')
            f *= c
        print('=', end='')
    if show == False:
        for c in range(x, 0, -1):
            f *= c
    return f
        

print(fatorial(3))
help(fatorial)