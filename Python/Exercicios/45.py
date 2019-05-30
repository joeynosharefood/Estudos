import random
print('Vamos jogar Jokenpo')
x = random.randrange(0, 3)
if x == 0:
    y = 'Pedra'
elif x == 1:
    y = 'Papel'
else:
    y = 'Tesoura'
z = str(input("""Escolha entre:
Pedra, Papel e Tesoura
"""))
if z == y:
    print('Empatou')
elif z in 'Pedrapedra':
    if y in 'Papel':
        print('Você perdeu, eu escolhi Papel')
    elif y in 'Tesoura':
        print('Você ganhou, eu escolhi Tesoura')
elif z in 'Tesouratesoura':
    if y in 'Pedra':
        print('Você perdeu, eu escolhi Pedra')
    elif y in 'Papel':
        print('Você ganhou, eu escolhi Papel')
elif z in 'Papelpapel':
    if y in 'Tesoura':
        print('Você perdeu, eu escolhi Tesoura')
    elif y in 'Pedra':
        print('Você ganhou, eu escolhi Pedra')