def ajuda(x):
    while True:
        h = str(input(x))
        help(h)
        brk = str(input('Deseja continuar ? '))
        if brk in 'Nn':
            break
    

ajuda('Deseja ajuda com qual função do python ?')

        