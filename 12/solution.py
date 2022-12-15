import math

Inf = math.inf

def easy_solution(name):
    points = {}
    rows = open(name).read().strip().split("\n")
    height = len(rows)
    width = len(rows[0])
    for i in range(height):
        for j in range(width):
            if rows[i][j] == 'S':
                points[(i,j)] = ['a', 0]
            else:
                points[(i,j)] = [rows[i][j], Inf]
    steps = 0
    while True:
        for x,y in points.keys():
            if points[(x,y)][1] == steps:
                for p in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                    if p in points.keys() and points[p][1] > steps:
                        if (ord(points[(x,y)][0]) + 1>= ord(points[p][0])) and points[p][0] > "Z":
                            points[p][1] = steps + 1
                        if points[(x,y)][0] in "yz" and points[p][0] == "E":
                            return steps + 1
        steps = steps + 1

def hard_solution(name):
    points = {}
    rows = open(name).read().strip().split("\n")
    height = len(rows)
    width = len(rows[0])
    for i in range(height):
        for j in range(width):
            if rows[i][j] == 'E':
                points[(i,j)] = ['z', 0]
            else:
                points[(i,j)] = [rows[i][j], Inf]
    steps = 0
    while True:
        for x,y in points.keys():
            if points[(x,y)][1] == steps:
                for p in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                    if p in points.keys() and points[p][1] > steps:
                        if points[(x,y)][0] == "b" and points[p][0] in "Sa":
                            return steps + 1                        
                        if (ord(points[p][0]) + 1 >= ord(points[(x,y)][0])) and points[p][0] > "Z":
                            points[p][1] = steps + 1

        steps = steps + 1

print(easy_solution("test-input"))
print(easy_solution("input"))
print(hard_solution("test-input"))
print(hard_solution("input"))
