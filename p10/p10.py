from math import sqrt, ceil

def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for d in range(2, ceil(sqrt(n))+1):
            if n % d == 0:
                return False
        return True

sumOfPrimes = 0
for i in range(1, 2000000):
    print(i)
    if isPrime(i):
        sumOfPrimes += i
print("Sum of primes below two million is " + str(sumOfPrimes))
