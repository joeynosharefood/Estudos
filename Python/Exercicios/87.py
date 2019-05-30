par =  maior = terceira = 0
m = []
l3 = [6, 7, 8]
l2 = [3, 4, 5]
for c in range(0, 9):
    x = int(input('Insira o valor: '))
    m.append(x)
    if c in l3:
        terceira += x
    if x % 2 == 0:
        par += x
    if c in l2:
        if maior < x:
            maior = x
h = 0
for ma in m:
    print(ma, end=" ")
    h += 1
    if h == 3:
        print('')
        h = 0
print(f'A soma dos valores da terceira linha é {terceira}')
print(f'O soma dos valores pares é {par}')
print(f'O maior número da segunda linha é {maior}')
