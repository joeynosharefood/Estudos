def voto(x):
    """
    """
    from datetime import datetime
    nascimento = int(input(x))
    ano = datetime.now()
    idade = ano.year - nascimento
    if idade < 18:
        return 'Não pode votar'
    if  65  > idade > 18:
        return 'Voto obrigatorio'
    else:
        return 'Voto opcional'

print(voto('Insira a sua idade aqui: '))

