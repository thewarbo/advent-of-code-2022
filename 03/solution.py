lines = [line.strip() for line in open("input").readlines()]

def priority(item):
    if item > "Z":
        return ord(item) - ord("a") + 1
    else:
        return ord(item) - ord("A") + 27

total = 0
def points(line):
    midpoint = len(line)//2
    item = list(set(line[0:midpoint]) & set(line[midpoint:]))[0]
    return priority(item)

def badge(idx):
    return list(set(lines[idx]) & set(lines[idx+1]) & set(lines[idx+2]))[0]


print("Part A: ", sum([points(line) for line in lines]))
print("Part B: ", sum([priority(badge(3 * idx)) for idx in range(len(lines) // 3)]))