x = int(input('Insira o ano de nascimento do nadador: '))
y = 2019 - x
print(y)
if y <= 9:
    print('Mirim')
elif y > 9 and y <= 14:
    print('Infantil')
elif y > 14 and y <= 19:
    print('Junior')
elif y == 20:
    print('Senior')
else:
    print('Master')