par = []
impar = []
conjunto = []
while True:
    x = int(input('Insira o número: '))
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
    brk = str(input('Deseja continuar ? '))
    if brk in 'Nn':
        break
conjunto.append(par.sort())
conjunto.append(impar.sort())
print(conjunto)
