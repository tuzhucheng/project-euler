# This version makes use of built-in Python functionalities

def isPalindrome(n):
    return str(n) == str(n)[::-1]

list = []
for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindrome(i*j):
            list = list + [i*j]

print(max(list))
