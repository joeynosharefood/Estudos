def contador(x, y, z):
    if x < y:
        y += 1
    if x > y:
        y -= 1
        z = z-(z*2)
    for c in range(x, y, z):
        print(c, end=' ')
    print()

contador(1, 10, 1)
contador(10, 0, 2)
x = int(input('Insira o inicio: '))
y = int(input('Insira o fim: '))
z = int(input('Insira o como vai pular: '))
contador(x, y, z)