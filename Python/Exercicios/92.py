cadastro = list()
temp = dict()
while True:
    temp['nome'] = str(input('Insira o nome: '))
    x = int(input('Insira o ano de nascimento: '))
    y = int(input('Insira nº de registro da carteira de trabalho: '))
    temp['ctps'] = y
    if y != 0:
        ano = int(input('Insira o ano de contratação: '))
        temp['sal'] = float(input('Insira o salario: '))
        temp['ano'] = ano
        temp['apose'] = 30+(ano-x)
    temp['idade'] = 2019-x
    brk = str(input('Deseja continuar ?'))
    cadastro.append(temp.copy())
    if brk in 'Nn':
        break
for c in cadastro:
        for k in c.items():
            print(f'O item {k[0]} tem valor {k[1]}')
