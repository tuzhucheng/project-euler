# This version avoids built-in functions, tries to do everything from scratch

def reverse(n):
    order = 1
    original = n

    while n >= 10:
        n = n // 10
        order = order * 10

    new = 0
    while order >= 1:
        new = original % 10 * order + new
        original = original // 10
        order = order // 10

    return new

def isPalindrome(n):
    n_reversed = reverse(n)
    if n == n_reversed:
        return True;
    else:
        return False;

def returnMax(l):
    maximum = 0
    for i in l:
        if i > maximum:
            maximum = i
    return maximum

list = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindrome(i*j):
            list = list + [i*j]

print(returnMax(list))
