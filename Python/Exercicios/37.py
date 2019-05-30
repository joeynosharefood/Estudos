x = float(input('Qual o salário do solicitante ?'))
y = float(input('Qual o valor do imovel ?'))
z = int(input('Em quantos anos pretende pagar ?'))
z1 = z*12
x1 = x*0.3
y1 = y/z1
if x1 >= y1:
    print('O valor a ser pago é de R${}'.format(y1))
else:
    print('O financiamento foi negado')