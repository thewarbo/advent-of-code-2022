import re
from math import lcm

def make_monkeys(filename):
    monkeys = open(filename).read().split("\n\n")
    result = []
    for monkey in monkeys:
        data = monkey.split("\n")
        name = re.search("Monkey (\d+):", data[0]).group(1)
        items = [int(item) for item in re.findall("\d+", data[1])]
        operation = re.search("Operation: new = (.+)$", data[2]).group(1)
        test = int(re.search("\d+", data[3]).group(0))
        good_monkey = int(re.search("\d+", data[4]).group(0))
        bad_monkey = int(re.search("\d+", data[5]).group(0))
        result.append([name, items, operation, int(test), (good_monkey, bad_monkey), 0])
    return result

def easy_solution(filename):
    monkeys = make_monkeys(filename)
    for round in range(20):
        for monkey in monkeys:
            for old in monkey[1]:
                new = int(eval(monkey[2]))
                item = new // 3
                if item % monkey[3] == 0:
                    monkeys[monkey[4][0]][1].append(item)
                else:
                    monkeys[monkey[4][1]][1].append(item)
                monkey[5] += 1
            monkey[1] = []
    counts = sorted([monkey[5] for monkey in monkeys], reverse = True)
    return counts[0] * counts[1]

def hard_solution(filename):
    monkeys = make_monkeys(filename)
    reducer = lcm(*[monkey[3] for monkey in monkeys])
    for round in range(10_000):
        for monkey in monkeys:
            for old in monkey[1]:
                new = int(eval(monkey[2]))
                item = new % reducer
                if item % monkey[3] == 0:
                    monkeys[monkey[4][0]][1].append(item)
                else:
                    monkeys[monkey[4][1]][1].append(item)
                monkey[5] += 1
            monkey[1] = []
    counts = sorted([monkey[5] for monkey in monkeys], reverse = True)
    return counts[0] * counts[1]

print("Easy Test: ", easy_solution("test-input"))
print("Easy Real: ", easy_solution("input"))
print("Hard Test: ", hard_solution("test-input"))
print("Hard Real: ", hard_solution("input"))