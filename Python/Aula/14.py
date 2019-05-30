n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par = n + par
    else:
        impar = n + impar
print(par)
print(impar)
print('Fim')
