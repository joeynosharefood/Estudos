h = 0
y = 0
x = str(input('Insira a sua expressão para verificar os parenteses: '))
for c in range(0, len(x)):
    if x[c] in '(':
        h += 1
    elif x[c] in ')':
        h -= 1
    if h == -1:
        y += 1
if h == 0:
    print('Sua equação está correta')
if h >= 1:
    print('Você não fechou todos parenteses')
if y >= 1:
    print('Você fechou parenteses a mais')