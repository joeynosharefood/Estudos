x = float(input('Insira a sua altura'))
y = float(input('Insira seu peso'))
z = y/(x*x)
if z < 18.5:
    print('abaixo do peso')
elif z >= 18.5 and z <= 25:
    print('peso ideal')
elif z > 25 and z <= 30:
    print('sobrepeso')
elif z > 30 and z <= 40:
    print('obesidade')
else:
    print('obesidade morbida')