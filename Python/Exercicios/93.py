jogador = dict()
jogador['nome'] = str(input('Insira o nome do jogador: '))
x = int(input('Quantos jogos ele participou ? '))
jogador['total'] = x
if x > 0:
    for c in range(1, x+1):
        jogador[c] = int(input(f'No jogo {c} ele marcou quantos gols ? '))
print('*'*50)
print(f'O jogador {jogador["nome"]} teve a seguinte participação')
print(f'Participou de um total de {jogador["total"]}')
if jogador['total'] > 0: 
    for c in range(1, jogador['total']+1):
        print(f'Na partida {c} ele fez {jogador[c]}')