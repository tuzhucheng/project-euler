# Commented lines are used to obtain the entire sequence

MAXIMUM_START = 1000000
max_length = 1
#max_sequence = []
max_length_start_number = 1

for start in range(1, MAXIMUM_START):
    i = start
    length = 1
    #sequence = [start]
    while i != 1:
        if i % 2 == 0:
            i = i//2
        else:
            i = 3*i + 1
        length += 1
        #sequence.append(i)
    if length > max_length:
        max_length = length
        #max_sequence = sequence
        max_length_start_number = start

print("Maximum length is " + str(max_length) + ".")
print("Start number of longest chain is " + str(max_length_start_number) + ".")
