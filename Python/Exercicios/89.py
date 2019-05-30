medias = []
temp = []
while True:
    nome = str(input('Insira o nome do aluno: '))
    a = float(input('Insira a primeira nota: '))
    b = float(input('Insira a segunda nota: '))
    ms = (a+b)/2
    temp = [nome, a, b, ms]
    medias.append(temp[:])
    temp.clear()
    brk = str(input('Deseja continuar ? '))
    if brk in 'Nn':
        break
for c in medias:
    for n, p in enumerate(c):
        if n == 0:
            print(p, end='.'*5)
        elif n == 3:
            print(p)
x = str(input('Deseja saber as notas de algum aluno ? '))
if x in 'Nn':
    print('Fim')
else:
    for h in medias:
        for a in h:
            if type(a) == str:
                if x in a:
                    print(f'O Aluno {h[0]} teve as seguinte nota na primeira prova {h[1]} e na segunda {h[2]} e sua média foi {h[3]}')
                else:
                    print('Não foi encontrado o aluno')



        
            


        