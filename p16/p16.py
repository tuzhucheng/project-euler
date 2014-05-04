s = 0
n = 2**1000
while n >= 1:
    r = n % 10
    s += r
    n //= 10
print("Sum of digits is {}.".format(s))
