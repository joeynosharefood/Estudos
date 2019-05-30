import random 
x = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), )
print(x)
x = sorted(x)
print(f'O maior valor é {x[4]} e o menor é {x[0]}')