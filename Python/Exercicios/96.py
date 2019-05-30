def area(a, b):
    m = a*b
    print(f'A aréa quadrada é {m}m²')

while True:
    x = float(input('Insira a largura: '))
    y = float(input('Insira o comprimento: '))
    area(x, y)
    brk = str(input('Deseja continuar ? '))
    if brk in 'Nn':
        break
