x = int(input('Qual o ano de nascimento do sujeito'))
x1 = 2019 - x
if x1 == 18:
    print('O sujeito tem q se alistar')
elif x1 < 18:
    x2 = 18 - x1
    print('Você precisa se alistar em {} anos'.format(x2))
else:
    x2 = x1 - 18
    print('Você tinha que se alistar em {} anos atrás'.format(x2))