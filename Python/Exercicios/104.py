def leia(x):
    j = 1
    while True:
        p = 0
        h = str(input(x))
        while p < len(h):
            if h[p] in '0123456789':
                j = 0
                break
            p +=1
        if j == 1:
            print('Você digitou errado')    
        if j == 0:
            break
leia('Insira o número inteiro: ')
