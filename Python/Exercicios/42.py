gasto = 0#somatoria de gastos
maisde1k = 0#somatori dos q custam mais de 1k
barato = ''#o nome do produto mais barato
vbarato = 0#o valor do produto mais barato
while True:
    x = str(input('Insira o nome do produto: '))
    y = float(input('Insir o valor do produto: '))
    gasto += y
    if y < 1000:
        maisde1k += 1
    if y < vbarato or vbarato == 0:
        vbarato += y
        barato = x
    p = str(input('Você deseja continuar ? '))
    if p in 'Nn':
        break
print(f'Foram gastos R${gasto}')
if maisde1k == 1:
    print(f'{maisde1k} produto custa mais de 1k')
else:
    print(f'{maisde1k} produtos custam mais de 1k')
print(f'O nome do produto mais barato é a {barato}')
