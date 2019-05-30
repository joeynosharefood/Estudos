import random
c = random.randrange(0, 10)
print(c)
n = 0
c1 = 0
c2 = 0
while n != 1:
    c1 = int(input('Qual o número que eu estou pensando ? '))
    c2 = c2 + 1
    if c1 == c:
        n = 1
print(c2)