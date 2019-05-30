c = 0
sexo = ''
while c != 1:
    sexo = str(input('Qual seu sexo (Insira o texto em maiusculo)? '))
    if sexo in 'M' or sexo in 'F':
        c = 1
print('fim')