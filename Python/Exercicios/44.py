x = float(input('Insira o valor do produto'))
y = int(input('Quantas parcelas'))
if y == 1:
    z = str(input("""Qual maneira de pagamento ?
    01 - Cheque/Dinheiro
    02 - Cartão
    """))
    if z == 1:
        z1 = x-(x*0.1)
        print('O valor a ser pago é de R${}'.format(z1))
    else:
        z1 = x-(x*0.5)
        print('O valor a ser pago é de R${}'.format(z1))
elif y == 2:
    z = x/y
    print('O valor a ser pago é de R${}'.format(z))
else:
    z = ((x*0.2)+x)/y
    print('O valor a ser pago é de R${}'.format(z))