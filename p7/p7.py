from math import sqrt

def isPrime(n):
    if (n <= 1):
        return False

    d = 2
    root = sqrt(n)
    while d <= root:
        if n % d == 0:
            return False
        d += 1

    return True

# start count from 1 (already counted 2), so we start to determine primes from 3
# this way we can check odd numbers only
count = 1
i = 3
while count < 10001:
    if isPrime(i):
        count += 1
    i += 2

i -= 2
print("The 10001st prime number is " + str(i))
