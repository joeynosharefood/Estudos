x = int(input('Digite um número inteiro: '))
y = int(input("""Escolha a base de Conversão usada:
1 - Binário
2 - Octal
3 - Hexadecimal
"""))
if y == 1:
    print('{} Convertido para Binário é igual a {}'.format(x, bin(x)[2:]))
elif y == 2:
    print('{} Convertido para Octal é igual a {}'.fomat(x, oct(x)[2:]))
else:
    print('{} Convertido para Hexadecimal é igual a {}'.format(x, hex(x)[2:]))