h = 0
h1 = 0
for c in range(0, 7):
    x = int(input('Insira o ano de nascimento: '))
    z = 2019 - x
    if z < 18:
        h += 1
    else:
        h1 += 1
print('{}maiores, {}menores'.format(h1, h))