x = 0
c = 0
h = 0
while True:
    x = int(input('Insira um valor : '))
    if x == 999:
        break
    h += x 
    c += 1
print(h)
print(c)