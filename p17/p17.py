single = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

teen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

double = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

under100 = []

under100.extend(single)
under100.extend(teen)
for i in double:
    under100.append(i)
    for j in single:
        under100.append(i + j)

words = []
words.extend(under100)

for i in single:
    hundred = i + 'hundred'
    words.append(hundred)
    for j in under100:
        words.append(hundred + 'and' + j)

words.append('onethousand')

print(words)

total_count = 0
for i in words:
    total_count += len(i)

print('Total: ' + str(total_count))
