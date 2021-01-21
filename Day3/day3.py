# AoC 2020 Day 3

with open('input.txt', 'r') as f:
    route_map = [path[:-1] for path in f.readlines()]

max_width = len(route_map[0])
max_height = len(route_map)

# Part 1
h = 0
w = 0
trees= 0

while h < max_height - 1:
    w += 3
    h += 1
    w = w - max_width if w >= max_width else w       
    trees += (1 if route_map[h][w] == '#' else 0)

print(trees)

# Part 2
max_width = len(route_map[0])
max_height = len(route_map)
# slope --> (moves right, moves down) ---> (x, y)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] 
mul_trees = 1

for x, y in slopes:
    h = 0
    w = 0
    trees = 0
    
    while h < max_height - y:
        w += x
        h += y
        w = w - max_width if w >= max_width else w
        trees += (1 if route_map[h][w] == '#' else 0)            
    mul_trees *= trees

print(mul_trees)


