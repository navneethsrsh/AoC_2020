# AoC 2020 Day 3 
# Solution 2: using collection deque
from collections import deque

with open('input.txt', 'r') as f:
    route_map = [path[:-1] for path in f.readlines()]

index = deque([x for x in range(len(route_map[0]))])
max_height = len(route_map)

# Part 1
h = 0
trees = 0

while h < max_height - 1:
    h += 1
    index.rotate(-3)
    trees += (1 if route_map[h][index[0]] == '#' else 0)

print(trees)

# Part 2
index = deque([x for x in range(len(route_map[0]))])
max_height = len(route_map)
# slope --> (moves right, moves down) ---> (x, y)
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] 
mul_trees = 1

for x, y in slopes:
    h = 0
    trees = 0
    
    while h < max_height - y:
        h += y
        index.rotate(-x)
        trees += (1 if route_map[h][index[0]] == '#' else 0)            
    mul_trees *= trees

print(mul_trees)
max_height = len(route_map)
