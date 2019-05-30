x = 0
for c in range (0, 501):
    z = c%2
    if z > 0:
        y = c%3
        if y == 0:
            x = x + c
print(x)