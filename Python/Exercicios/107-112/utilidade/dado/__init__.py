def leiadinheiro(x, y, z):
    from utilidade import moeda
    valor = 0
    ok = False
    while True:
        n = str(input(x))
        if n.isnumeric():
            x = int(n)
            ok = True
        else:
            print('Valor errado')
        if ok:
            break
    return moeda.resumo(x, y, z)