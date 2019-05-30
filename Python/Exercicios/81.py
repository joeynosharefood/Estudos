y = []
h = 0
c = 0
while True:
    x = int(input('Insira o valor aqui: '))
    y.append(x)
    c += 1
    if x == 5:
        h += 1
    k = str(input('Deseja continuar ? '))
    if k in 'Nn':
        break
y = sorted(y, reverse=True)
if c == 1:
    print('Foi digitado somente um valor')
else:
    print(f'Foram digitados {c} valores')
print(f'O valores digitados em forma decrescente foram {y}')
if h == 0:
    print('Não foi inserido o valor 5')
else:
    print('O valor 5 foi digitado')
   