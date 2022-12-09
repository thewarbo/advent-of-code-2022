def easy_solution(file):
    lines = [line.strip() for line in open(file).readlines()]
    line_length = len(lines[0])
    grid = [[int(character) for character in line] for line in lines]
    visible_count = 0
    for i in range(len(grid)):
        for j in range(line_length):
            print(i, j, grid[i][j], grid[i][j+1:])
            if i == 0 or j == 0 or i == line_length - 1 or j == len(grid) -1:
                visible_count += 1
            elif grid[i][j] > max(grid[i][:j]):
                visible_count += 1
            elif grid[i][j] > max(grid[i][j+1:]):
                visible_count += 1
            elif grid[i][j] > max([grid[k][j] for k in range(i)]) or grid[i][j] > max([grid[k][j] for k in range(i+1, line_length)]):
                visible_count += 1


    return visible_count

def sight_length(x):
    x = list(x)
    if len(x) == 1:
        return 0
    for i in range(1,len(x)):
        if x[i] >= x[0]:
            return i
    return len(x) - 1
            

def hard_solution(file):
    lines = [line.strip() for line in open(file).readlines()]
    line_length = len(lines[0])
    grid = [[int(character) for character in line] for line in lines]
    best_scenery = 0
    for i in range(len(grid)):
        for j in range(line_length):
            distances = [sight_length(grid[i][j:]) , \
                sight_length(reversed(grid[i][:j+1])) , \
                sight_length(reversed([grid[k][j] for k in range(0, i+1)])) , \
                sight_length([grid[k][j] for k in range(i, line_length)])]
            current_scenery = distances[0] * distances[1] * distances[2] * distances[3]
            best_scenery = max(best_scenery, current_scenery)



    return best_scenery

print("Test: ", easy_solution("test-input"))
print("Real: ", easy_solution("input"))
print("Test: ", hard_solution("test-input"))
print("Real: ", hard_solution("input"))
