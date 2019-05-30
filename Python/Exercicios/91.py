from random import randint
temp = dict()
jogadores = list()
maior = 0
while True:
    temp['jogador'] = str(input('Insira o nome do jogador: '))
    x = randint(1, 7)
    if x > maior:
        maior = x
    temp['rolada'] = x
    jogadores.append(temp.copy())
    brk = str(input('Deseja continuar ? '))
    if brk in 'Nn':
        break
for j in jogadores:
    print('O jogador ', j['jogador'], 'tirou', j['rolada'], 'no dado.', end=' ')
print()
for h in jogadores:
    if h['rolada'] == maior:
        print(f'Portanto o jogador ganhador foi {h["jogador"]} sendo que ele tirou {h["rolada"]} no dado.')

