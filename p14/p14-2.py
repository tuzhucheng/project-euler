MAXIMUM_START = 1000000
max_length = 1
max_length_start_number = 1
length_dict = {} # dictionary that maps start number to length

for start in range(1, MAXIMUM_START):
    i = start
    length = 1
    while i != 1:
        if i % 2 == 0:
            i = i//2
        else:
            i = 3*i + 1

        if i in length_dict:
            length += length_dict[i]
            break
        else:
            length += 1

    length_dict[start] = length

    if length > max_length:
        max_length = length
        max_length_start_number = start

print("Maximum length is " + str(max_length) + ".")
print("Start number of longest chain is " + str(max_length_start_number) + ".")
