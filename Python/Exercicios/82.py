x = []
y = []
z = []
while True:
    k = int(input('Insira o valor aqui: '))
    x.append(k)
    if k%2 == 0:
        y.append(k)
    else:
        z.append(k)
    j = str(input('Você deseja continuar ?'))
    if j in 'Nn':
        break
print(f'Você digitou os seguintes números {x}, sendo', end='')
if len(y) >= 2:
    print(f' o conjunto de números par {y} ', end='')
else:
    print(f' somente um número par {y} ', end='')
if len(z) >= 2:
    print(f'e o conjunto de números impares {z}')
else:
    print(f'e sendo somente um número impar {z}')