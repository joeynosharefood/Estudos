c = 0
h = 0
b = 0
while c != 1:
    c = int(input('Insira os valores(se quiser parar digite 999)'))
    if c != 999:
        h += c
        b += 1
    else:
        c = 1
print(h)
print(b)