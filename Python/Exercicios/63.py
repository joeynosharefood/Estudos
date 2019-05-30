x = int(input('Insira o primeiro termo: '))
y = int(input('A razão é: '))
c = 0
print(x)
while c != 10:
    x = y+x
    c += 1
    print(x)
    if c == 9:
        x = y+x
        print(x)
        h = int(input('Quantos termos você gostaria de ver a mais ? '))
        if h == 0:
            c += 1
        else:
            h -= 1
            c = c - h