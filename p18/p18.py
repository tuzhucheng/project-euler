pyramid = []
with open('pyramid.txt', 'r') as f:
    for line in f:
        l = []
        for value in line.split():
            l.append({'value':int(value)})
        pyramid.append(l)

height = len(pyramid)
pyramid[0][0]['accumulated'] = (pyramid[0][0]['value'], 0)
for row_index, row in enumerate(pyramid[1:height], start=1):
    for node_index, node in enumerate(row):
        if node_index == 0:
            parent_left = (0, 0)
            parent_right = pyramid[row_index-1][node_index]['accumulated']
        elif node_index == len(row)-1:
            parent_left = pyramid[row_index-1][node_index-1]['accumulated']
            parent_right = (0, 0)
        else:
            parent_left = pyramid[row_index-1][node_index-1]['accumulated']
            parent_right = pyramid[row_index-1][node_index]['accumulated']

        accumulate_left = max(parent_left) + node['value']
        accumulate_right = max(parent_right) + node['value']
        node['accumulated'] = (accumulate_left, accumulate_right)

candidates = []
for node in pyramid[height-1]:
    candidates.append(max(node['accumulated']))

print('The answer is {}.'.format(max(candidates)))

