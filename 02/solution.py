f=open("input")
lines = f.readlines()

def total_points_easy(line):
    points = ord(line[2]) - ord("W")
    points += (3 * ((ord(line[2]) - ord(line[0]) - 1) % 3))
    return(points)

def total_points_hard(line):
    points = 3 * (ord(line[2]) - ord("X"))
    points += ((ord(line[0]) + ord(line[2]) - 1) % 3) + 1
    return(points)


print("Part 1: ", sum([total_points_easy(line) for line in lines]))
print("Part 2: ", sum([total_points_hard(line) for line in lines]))