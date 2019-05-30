m = []
for c in range(0, 9):
    m.append(int(input('Insira o valor: ')))
h = 0
for ma in m:
    print(ma, end=" ")
    h += 1
    if h == 3:
        print('')
        h = 0

