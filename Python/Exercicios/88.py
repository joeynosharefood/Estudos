from random import randint
x = int(input('Quantos jogos vão ser ? '))
jogos = []
temp = []
for c in range(0, x):
    for c in range(0, 6):
        temp.append(randint(0, 60))
    jogos.append(temp[:])
    temp.clear()
print(jogos)