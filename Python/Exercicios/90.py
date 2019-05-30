alunos = list()
temp = dict()
while True:
    temp['nome'] = str(input('Insira o nome: '))
    p1 = float(input('Insira a nota da P1: '))
    p2 = float(input('Insira a nota da P2: '))
    media = (p1+p2)/2 
    temp['p1'] = p1
    temp['p2'] = p2
    temp['media'] = media
    alunos.append(temp.copy())
    brk = str(input('Deseja continuar ?'))
    if brk in 'Nn':
        break
x = str(input('Busque a notas cadastradas pelo nome do aluno: '))
for a in alunos:
    for k in a.values():
        if x == k:
            print(a)