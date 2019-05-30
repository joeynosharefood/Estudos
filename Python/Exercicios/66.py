c = 0
somatoria = 0
maior = 0 
menor = 1000000000000000
total = 0
while c != 1:
    x = int(input('Insira o valor: '))
    somatoria += x
    total +=1
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    h = str(input('Vc pretende continuar ? '))
    if h in 'Nn':
        c = 1
print(somatoria/total)
print(maior)
print(menor)