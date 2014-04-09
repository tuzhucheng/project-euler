summation = 0
with open('p13_input.txt') as f:
    for line in f:
        summation += int(line)

summation = str(summation)
print("The sum is {}.".format(summation))
print("The first ten digits are {}.".format(summation[:10]))
