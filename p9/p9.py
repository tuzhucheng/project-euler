possibilities = []
for c in range(1, 1000):
    for b in range(1, c):
        a = 1000 - c - b
        if a > 0 and a < b and b < c:
            if a**2 + b**2 == c**2:
                print('{0}^2 + {1}^2 = {2}^2 and {0} + {1} + {2} = 1000'.format(a, b, c))
                print('The product is {0}.'.format(a*b*c))
