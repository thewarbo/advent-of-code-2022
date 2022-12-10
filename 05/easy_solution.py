import re

def fix_initial(x):
    lines = x.split("\n")
    piles = {}
    for idx in range(1, len(lines[-1]), 4):
        piles[lines[-1][idx]] = [line[idx] for line in lines[-2::-1] if line[idx] != ' ']
    return piles

initial, moves = open("input").read().split("\n\n")
piles = fix_initial(initial)
# print(piles)
for move in moves.strip().split("\n"):
    count, origin, target = move.split(" ")[1::2]
    for idx in range(int(count)):
        piles[target].append(piles[origin].pop())


for label in sorted(piles.keys()):
    print(piles[label][-1], end = "")
print()