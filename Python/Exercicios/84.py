c = maior = menor = 0
temp = []
cadastro = []
while True:
    n = str(input('Insira o nome da pessoa: '))
    p = float(input('Insira o peso da pessoa: '))
    if maior < p :
        maior = p
    if menor > p or menor == 0 :
        menor = p
    temp = [n, p]
    cadastro.append(temp[:])
    temp.clear()
    c += 1
    brk = str(input('Deseja continuar ?  '))#breakpoint 
    if brk in 'Nn':
        break
print(f'Foram cadatrados {c} pessoas')
print(f'As pessoas com maior peso são', end=' ')
for mais in cadastro:
    if mais[1] == maior:
        print(mais[0], end=' ')
print('')
print(f'As pessoas com o menor peso são', end=' ')
for men in cadastro:
    if men[1] == menor:
        print(men[0], end=' ')
