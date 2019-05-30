x = float(input('Insira a primeira nota: '))
y = float(input('Insira a segunda nota : '))
z = (x+y)/2
print(z)
if z < 5:
    print('Está reprovado')
elif 5 == z < 7:
    print('Está de recuperação')
elif z == 6.9:
    print('Está de recuperação')
elif z >= 7:
    print('Está aprovado')