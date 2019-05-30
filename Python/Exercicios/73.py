import time
camp = ('Flamengo', 'Santos', 'Palmeiras', 'São Paulo', 'Corinthians', 'BotaFogo', 'Chapecoense')
print(len(camp))
print('Os Cinco primeiros colocados são: ')
for c in range(0, 5):
    print(camp[c])
print('')
print('Os Quatro ultimos colocados são: ')
for c in range(6, 2, -1):
    print(camp[c])
print('')
x = camp.index('Chapecoense')
print(f'O Chapecoense está na colocação de número {x}')