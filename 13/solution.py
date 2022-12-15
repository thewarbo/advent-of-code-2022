from functools import cmp_to_key

def compare(first, second):
    if type(first) == int and type(second) == int:
        return (first < second) - (second < first)
    if type(first) == list and type(second) == list:
        for i in range(min(len(first), len(second))):
            if compare(first[i], second[i]):
                return compare(first[i], second[i])
        return compare(len(first), len(second))
    if type(first) == list and type(second) == int:
        return compare(first, [second])
    if type(first) == int and type(second) == list:
        return compare([first], second)
    return "Error"
            

def easy_solution(filename):
    pairs = open(filename).read().strip().split("\n\n")
    result = 0
    for i in range(len(pairs)):
        first, second = pairs[i].split("\n")
        if compare(eval(first), eval(second)) == 1:
            result += i +1
    return result

def hard_solution(filename):
    pairs = open(filename).read().strip().split("\n")
    pairs = filter(lambda x : x, pairs)
    pairs = map(eval, pairs)
    pairs = list(pairs)
    pairs.extend([[[2]], [[6]]])
    pairs.sort(key=cmp_to_key(compare), reverse = True)
    return (pairs.index([[2]]) +1)* (pairs.index([[6]]) +1 )

print(easy_solution("test-input"))
print(easy_solution("input"))
print(hard_solution("test-input"))
print(hard_solution("input"))
