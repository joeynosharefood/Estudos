t = (int(input('Insira um numero')),
    int(input('Insira um numero')),
    int(input('Insira um numero')),
    int(input('Insira um numero')))
print(t)
print(t.count(9))
print(t.index(3))
for c in range(0, 4):
    if t[c]%2 == 0:
        print(t[c])

