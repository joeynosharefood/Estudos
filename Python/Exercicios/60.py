n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
c = 0
op = 0
while c != 5:
    op = int(input("""Você deseja:
    [1] Somar
    [2] Multiplicar
    [3] Maior valor entre os dois
    [4] Novos números
    [5] Sair do programa
    """))
    if op == 1:
        print('{}+{}={}'.format(n1, n2, n1+n2))
    elif op == 2:
        print('{}x{}={}'.format(n1, n2, n1*n2))
    elif op == 3:
        h = n1 < n2
        print(h)
        if h is True:
            print(n2)
        elif n1 == n2:
            print('Os dois números são iguais')
        else:
            print(n1)
    elif op == 4:
        n1 = int(input('Insira um novo primeiro valor: '))
        n2 = int(input('Insira um novo segundo valor: '))
    else:
        c = op