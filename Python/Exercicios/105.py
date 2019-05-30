def nota(*x):
    """
    """
    ltemp = list(x)
    ltemp = sorted(ltemp)
    qnt = len(ltemp)
    c = 0
    media = 0
    while c < len(ltemp):
        media += ltemp[c]
        c += 1
    media = media/qnt
    situacao = ''
    if media < 5:
        situacao = 'Ruim'
    if 7 > media >= 5:
        situacao = 'Boa'
    if media > 7:
        situacao = 'Muito Boa'
    dct = {'Quantidade': qnt, 'Maior Nota': ltemp[-1], 
    'Menor Nota': ltemp[0], 'Media': media, 'Situacao':situacao
    }
    notas = [dct.copy()]
    print(notas)
    
nota(2, 1, 0)