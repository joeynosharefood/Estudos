maior = 0
menor = 1000
for c in range(0, 5):
    x = float(input('Insira o peso: '))
    if x > maior:
        maior = x
    if x < menor:
        menor = x
print(maior)
print(menor)