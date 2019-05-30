y = []
for c in range(0, 5):
    x = int(input('Insira o valor aqui:'))
    if c == 0 or x > y[-1]:
        y.append(x)
    else:
        pos = 0 
        while pos < len(y):
            if x <= y[pos]:
                y.insert(pos, x)
                break
            pos += 1
print(y)    
