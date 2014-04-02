# a will store the sum of squares
a = 0
for i in range(1, 101):
    a = a + i**2
print("The sum of squares of the first 100 natural numbers is " + str(a))

# b will store the square of sum
b = 0;
for i in range(1, 101):
    b = b + i
b = b**2
print("The square of the sum of the first 100 natural numbers is " + str(b))

print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is " + str(b-a) + ".")
