pyramid = []
with open('pyramid.txt', 'r') as f:
    for line in f:
        l = []
        for value in line.split():
            l.append(int(value))
        pyramid.append(l)

height = len(pyramid)
for row_index, row in enumerate(pyramid[1:height], start=1):
    for node_index, node in enumerate(row):
        if node_index == 0:
            row[node_index] = pyramid[row_index-1][node_index] + node
        elif node_index == len(row)-1:
            row[node_index] = pyramid[row_index-1][node_index-1] + node
        else:
            parent_left = pyramid[row_index-1][node_index-1]
            parent_right = pyramid[row_index-1][node_index]
            row[node_index] = max(parent_left, parent_right) + node

print('The answer is {}.'.format(max(pyramid[height-1])))

