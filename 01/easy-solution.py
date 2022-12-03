import itertools

f = open("input")
lines = f.readlines()

current_elf = 0
max_elf = 0

for line in lines:
    if line == '\n':
        if current_elf > max_elf:
            max_elf = current_elf
        current_elf = 0
    else:
        current_elf += int(line)

print(max_elf)
