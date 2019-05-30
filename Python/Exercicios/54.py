x = str(input('Digite a frase: ')).upper().replace(' ','')
print(x)
if x == x[::-1]:
    print('É um palindromo')
else:
    print('Não é um palindromo')