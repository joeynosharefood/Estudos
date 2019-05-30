y = []
for c in range(0, 5):
    y.append(int(input('Insira o valor aqui: ')))
x = y[:]
x = sorted(x)
p = y.index(x[4])
p2 = y.index(x[0])
print(f'Na posição {p} está o maior número que é {x[4]}')
print(f'Na posição {p2} está o menor número que é {x[0]}')