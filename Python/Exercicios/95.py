h = 0
cadastro = list()
temp = dict()
while True:
    nome = str(input('Insira o nome: '))
    total = int(input('Quantos jogos ele participou ? '))
    temp = {'nome': nome, 'total':total}
    if total > 0:
        for jogos in range(1, total+1):
            temp[jogos] = int(input(f'No jogo {jogos} ele marcou quantos gols ?'))
    cadastro.append(temp.copy())
    brk = str(input('Deseja continuar ?'))
    if brk in 'Nn':
        break
print('***'*20)
for cad in cadastro:
    for k, v in cad.items():
        if k == 'nome':
            print(f'O jogador {v}')
        if k == 'total':
            print(f'Jogou um total de {v} jogos')
        if type(k) == int:
            print(f'No jogo de número {k} ele marcou {v} gols')
    print()
print('***'*20)
while True:
    busca = str(input('Deseja saber sobre qual jogador ? '))
    print('***'*20)
    for jogador in cadastro:
        if busca == jogador['nome']:
            print(f'O jogador {jogador["nome"]} jogou em ', end='')
            print(jogador['total'])
            if jogador['total'] > 0:
                for jogos in range(0, jogador['total']):
                    print(f'No jogo {jogos+1} ele marcou {jogador[jogos+1]}')
            h = 1
    if h == 0:
        print('Não achei')
    print()
    brk = str(input('Deseja continuar ?'))
    if brk in 'Nn':
        break
