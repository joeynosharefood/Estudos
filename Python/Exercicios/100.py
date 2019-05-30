def sorteio(x):
    from random import randint
    for c in range(0, 5):
        x.append(randint(0, 10))
def somapar(x):
    soma = 0
    for c in x:
        if c%2 == 0:
            soma += c
    print(soma)
num = list()
sorteio(num)
print(num)
somapar(num)

