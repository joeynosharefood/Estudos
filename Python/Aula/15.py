n = c = 0
while True:
    c = int(input('Insira o valor: '))
    if c != 999:
        n += c
    else: 
        break
print(f'A soma vale {n}')
