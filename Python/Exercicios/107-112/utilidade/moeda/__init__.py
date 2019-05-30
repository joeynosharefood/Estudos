def moeda(x=0, y='R$'):
    """
    Ele formata para um formato monetario utilizando a função .replace
    by JoeyNoShareFood
    """
    return f'{y} {x:.2f}'.replace('.', ',')   
def aumentar(x, y=0, show= False):
    """
    Você insere no valor de x o valor a ser aumentado,
    em y você envia a porcentagem selecionada para o aumento.
    Uma variavel iniciada como 'porc' recebe o valor de y
    multiplicando por 0.01 um valor que quando multiplicado vai me devolver um valor de 0.00(0%)
    à 1.00(100%), como padrão ele vai receber um valor de 0, Esse valor é multiplicado pelo valor inserido em 
    x, portando (x*porc)+x que me retorna o resultado.
    by JoeyNoShareFood
    """
    porc = y*0.01
    x += (x * porc)
    if show == False:
        return x
    if show == True:
        return moeda(x)
def diminuir(x, y=0, show= False):
    """
    Você insere no valor de x o valor a ser aumentado,
    em y você envia a porcentagem selecionada para a diminuição.
    Uma variavel iniciada como 'porc' recebe o valor de y
    multiplicando por 0.01 um valor que quando multiplicado vai me devolver um valor de 0.00(0%)
    à 1.00(100%), como padrão ele vai receber um valor de 0, Esse valor é multiplicado pelo valor inserido em 
    x, portando x-(x*porc) que me retorna o resultado.
    by JoeyNoShareFood
    """
    porc = y*0.01
    x -= (x* porc)
    if show == False:
        return x
    if show == True:
        return moeda(x)
def dobro(x=0, show= False):
    """
    Você insere no valor de x o valor a ser dobrado.
    by JoeyNoshareFood
    """
    x += x
    if show == False:
        return x
    if show == True:
        return moeda(x)
def metade(x=0, show=False):
    """
    Você insere o valor de x o valor que vai ser retornado é a metade
    by JoeyNoShareFood
    """
    x /= 2
    if show == False:
        return x
    if show == True:
        return moeda(x)
def resumo(valor,aum, dim):
    x = 'O Resumo do Modulo Moeda'
    print('*'*(len(x)+20))
    print('        ', x)
    print('*'*(len(x)+20))
    print(f'O valor digitado {moeda(valor)}')
    print(f'A metade do valor {metade(valor, True)}')
    print(f'O dobro do valor {dobro(valor, True)}')
    print(f'O valor com {aum}% {aumentar(valor, aum, True)}')
    print(f'O valor com menos {dim}% {diminuir(valor, dim, True)}')
    print('*'*(len(x)+20))

