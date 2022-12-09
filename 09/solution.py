def signum(x):
    return x and x//abs(x)

def easy_solution(file):
    visited = {(0,0)}
    head = [0,0]
    tail = [0,0]
    for line in open(file).readlines():
        [direction, distance] = line.split()
        for idx in range(int(distance)):
            if direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1
            elif direction == 'U':
                head[1] += 1
            elif direction == 'D':
                head[1] -= 1
            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                tail[0] += signum(head[0] - tail[0])
                tail[1] += signum(head[1] - tail[1])
            visited.add(tuple(tail))     
    return len(visited)


def hard_solution(file):
    visited = {(0,0)}
    rope = [[0,0] for i in range(10)]
    for line in open(file).readlines():
        [direction, distance] = line.split()
        for idx in range(int(distance)):
            if direction == 'R':
                rope[0][0] += 1
            elif direction == 'L':
                rope[0][0] -= 1
            elif direction == 'U':
                rope[0][1] += 1
            elif direction == 'D':
                rope[0][1] -= 1
            for i in range(9):
                if abs(rope[i][0] - rope[i+1][0]) > 1 or abs(rope[i][1] - rope[i+1][1]) > 1:
                    rope[i+1][0] += signum(rope[i][0] - rope[i+1][0])
                    rope[i+1][1] += signum(rope[i][1] - rope[i+1][1])
            visited.add(tuple(rope[i+1]))     
    return len(visited)



print("Test: ", easy_solution("test-input"))
print("Real: ", easy_solution("input"))
print()
print("Test: ", hard_solution("test-input"))
print("Real: ", hard_solution("input"))