import itertools

f = open("input")
lines = f.readlines()

current_elf = 0
elves = list()

for line in lines:
    if line == '\n':
        elves.append(current_elf)
        current_elf = 0
    else:
        current_elf += int(line)

print(sum(sorted(elves, reverse = True)[0:3]))
