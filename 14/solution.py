def go_towards(pt1, pt2):
    return (pt1[0] + (pt2[0] > pt1[0]) - (pt2[0] < pt1[0]), pt1[1] + (pt2[1] > pt1[1]) - (pt2[1] < pt1[1])) 

def display(occupied):
    for y in range(10):
        for x in range(494, 504):
            if (x,y) in occupied.keys():
                if occupied[(x,y)] == "s":
                    print("o", end = "")
                elif occupied[(x,y)] == "r":
                    print("#", end = "")
                else:
                    print(" ", end = "")
            else:
                print(".", end = "")
        print()


def easy_solution(filename):
    lines = open(filename).readlines()
    occupied = {}
    for line in lines:
        text_vertices = line.split(" -> ")
        vertices = []
        for vertex in text_vertices:
            x,y = vertex.split(",")
            vertices.append((int(x), int(y)))
        for idx in range(len(vertices) - 1):
            pos = vertices[idx]
            while pos != vertices[idx+1]:
                occupied[pos] = "r"
                pos = go_towards(pos, vertices[idx+1])
            occupied[pos] = "r"
    abyss = max(y for x,y in occupied.keys())
    falling = (500,0)
    while falling[1] < abyss:
        if not (falling[0], falling[1] + 1) in occupied.keys():
            falling = (falling[0], falling[1] + 1)
        elif not (falling[0] - 1, falling[1] + 1) in occupied.keys():
            falling = (falling[0] - 1, falling[1] + 1)
        elif not (falling[0] + 1, falling[1] + 1) in occupied.keys():
            falling = (falling[0] + 1, falling[1] + 1)
        else:
            occupied[falling] = "s"
            falling = (500,0)
            # display(occupied)
    return sum([v=="s" for v in occupied.values()])

def hard_solution(filename):
    lines = open(filename).readlines()
    occupied = {}
    for line in lines:
        text_vertices = line.split(" -> ")
        vertices = []
        for vertex in text_vertices:
            x,y = vertex.split(",")
            vertices.append((int(x), int(y)))
        for idx in range(len(vertices) - 1):
            pos = vertices[idx]
            while pos != vertices[idx+1]:
                occupied[pos] = "r"
                pos = go_towards(pos, vertices[idx+1])
            occupied[pos] = "r"
    abyss = max(y for x,y in occupied.keys())
    falling = (500,0)
    while not falling in occupied.keys():
        if falling[1] == abyss + 1:
            occupied[falling] = "s"
            falling = (500,0)
        if not (falling[0], falling[1] + 1) in occupied.keys():
            falling = (falling[0], falling[1] + 1)
        elif not (falling[0] - 1, falling[1] + 1) in occupied.keys():
            falling = (falling[0] - 1, falling[1] + 1)
        elif not (falling[0] + 1, falling[1] + 1) in occupied.keys():
            falling = (falling[0] + 1, falling[1] + 1)
        else:
            occupied[falling] = "s"
            falling = (500,0)
            # display(occupied)
    return sum([v=="s" for v in occupied.values()])

print(easy_solution("test-input"))
print(easy_solution("input"))
print(hard_solution("test-input"))
print(hard_solution("input"))



