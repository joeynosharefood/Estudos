media = 0
maisvelho = 0
nomem = ''
h = 0
for c in range (0, 4):
    nome = str(input('Insira o nome: '))
    idade = int(input('Insira a idade: '))
    sexo = str(input('Insira o sexo(M/F): '))
    media = idade + media
    if idade > maisvelho and sexo in 'Mm':
        maisvelho = idade + maisvelho
        nomem = nome
    if idade < 20 and sexo in 'Ff':
        h = h + 1
print(media/4)
print(nomem)
print(h)