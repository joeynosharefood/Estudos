def maior(x):
    mr = 0
    lista = list()
    while True:
        valor = int(input(x))
        lista.append(valor)
        if valor > mr:
            mr = valor
        brk = str(input('Deseja continuar ? '))
        if brk in 'Nn':
            break
    print(mr)





maior('Insira o valor: ')


