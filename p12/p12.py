from math import sqrt

def countFactors(n):
    factors = []
    divisor = 1
    rt = sqrt(n)
    while divisor <= rt:
        if n % divisor == 0:
            factors.append(divisor)
            if divisor != rt:
                factors.append(n/divisor)
        divisor += 1
    return len(factors)

def main():
    index = 1
    triangle = 1
    while countFactors(triangle) < 500:
        index += 1
        triangle += index

    print("The first triangle number to have over 500 divisors is {}.".format(triangle))

if __name__ == "__main__":
    main()
