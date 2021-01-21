# AoC 2020 Day 3

with open('input.txt', 'r') as f:
    route_map = [path[:-1] for path in f.readlines()]

max_width = len(route_map[0])
max_height = len(route_map)

# Part 1
h = 0
w = 0
extend = 1
trees = 0
traverse = [path for path in route_map]

while h < max_height - 1:
    if w + 3 >= max_width:
        extend += 1
        traverse = [path * extend for path in route_map]
        
    if traverse[h + 1][w + 3] == '#':
        trees += 1
    w  += 3
    h += 1

print(trees)

# Part 2
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
mul_trees = 1
max_width = len(route_map[0])
max_height = len(route_map)

for x, y in slopes:
    h = 0
    w = 0
    trees = 0
    extend = 1
    traverse = [path for path in route_map]
    print(x,y)
    while h < max_height - y:
        if w + x >= max_width:
            extend += 1
            traverse = [path * extend for path in route_map]
            
        if traverse[h + y][w + x] == '#':
            trees += 1
        w  += x
        h += y
    mul_trees *= trees

print(trees)


