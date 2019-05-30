z = 0#variavel iniciada para demonstrar qnts tem +18
h = 0#variavel iniciada para demosntra quantos homens foram cadastrados
u = 0#variavel iniciada para demonstrar quantas mulheres tem menos de 20 anos
while True:
    x = str(input('Insira o sexo: ').upper())
    y = int(input('Insira a idade: '))
    if y > 18:
        z += 1
    if x == 'M':
        h += 1
    if x == 'F' and y < 20:
        u += 1
    p = str(input('Você deseja continuar ? '))
    if p in 'NãonãonaoNaonN':
        break
print(f'{z} tem mais de 18 anos')
print(f'{h} homens foram cadastrados')
print(f'{u} mulheres cadastradas tem menos de 20 anos')
