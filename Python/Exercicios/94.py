acima = list()#acima da media
mulheres = list()#mulheres
cadastro = list()#lista geral
temp = dict()#dicionario temporario
idade = total = media = 0#soma para media da idade/total de cadastrados/media de idade
while True:
    x = str(input('Insira o nome: '))
    y = str(input('Insira o sexo: '))
    z = int(input('Insira a idade: '))
    total += 1
    idade += z
    if total > 1:
        media = idade/total
    if y in 'Ff':
        mulheres.append(x)
    temp = {'nome':x, 'sexo':y, 'idade':z}
    cadastro.append(temp.copy())
    brk = str(input('Deseja continuar ? '))
    if brk in 'Nn':
        break
for k in cadastro:
    if k['idade'] > media:
        acima.append(k.copy())
print('*'*20)
print('Todos cadastros')
for cad in cadastro:
    print(cad)
print('*'*20)
print('Todas mulheres cadastradas')
for mul in mulheres:
    print(mul)
print('*'*20)
print('Todas as pessoas acima da media de idade')
for ac in acima:
    print(ac)
print('*'*20)
print(f'O total de cadastrados efetuados foram {total}')

