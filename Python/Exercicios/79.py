y = []
while True:
    x = int(input('Insira o valor aqui: '))
    if x in y:
        k = str(input('Deseja continuar ?'))
        if k in 'Nn':
            break
    else:
        y.append(x)
        k = str(input('Deseja continuar ?'))
        if k in 'Nn':
            break
print(y)