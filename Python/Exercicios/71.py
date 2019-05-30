cc = cv = cd = cu = 0#Cedulas de 50, 20, 10 e 1 nessa ordem
x = int(input('Insira o valor a ser sacado: '))
while True:
    if x >= 50:
        x = x - 50
        cc += 1
        if x == 0:
            break
    if x >= 20 and x < 50:
        x = x - 20
        cv += 1
        if x == 0:
            break
    if x >= 10 and x < 20:
        x = x - 10
        cd += 1 
        if x == 0:
            break
    if x >= 1 and x < 10:   
        x = x - 1
        cu += 1
        if x == 0:
            break
print(f'Notas de 50: {cc}')
print(f'Notas de 20: {cv}')
print(f'Notas de 10: {cd}')
print(f'Notas de 1: {cu}')