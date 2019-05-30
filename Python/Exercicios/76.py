produtos = 'Batata', 5.00, 'Bolacha', 2.00, 'Ervilha', 6.0, 'Pacote Maria', 0.5
for c in range(0, len(produtos)):
    if c%2 == 0:
        x = y = len(produtos[c])
        x = 50-(x+x+1)
        y = y + x
        print(produtos[c], '.'*y, produtos[c+1])