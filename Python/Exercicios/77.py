p = 'Banana', 'Batata', 'Piroca'
for c in range(len(p)):
    x = p[c]
    print(f'{x} tem as seguintes vogais', end=' ')
    for k in range(len(x)):
        if x[k] in 'aeiou':
            print(x[k], end=' ')
    print('')
