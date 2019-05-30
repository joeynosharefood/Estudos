x = int(input('Insira seu número aqui: '))
y = 0#o y vai receber 1 valor somado toda vez que for divisivel o número inserido no x
if x == 0 or x == 1:
    print('Seu número não é primo')
else:
    h = x % 2
    if h > 0 and x > 2:#como 2 não é primo se usa como base, porém se ele for divisvel por 2 ele também não é primo, já que ele só pode ser divisivel por ele mesmo
        y = 2
    if y == 2:
        print('Seu número é primo')
    else:
        print('Seu número não é primo')