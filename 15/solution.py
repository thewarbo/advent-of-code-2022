import re

input_format = re.compile("Sensor at x=(\-?\d+), y=(\-?\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)")

def easy_solution(filename, target):
    lines = open(filename).readlines()
    coords = []
    for line in lines:
        x = re.search(input_format, line)
        coords.append( list(int(coord) for coord in x.groups()))
    sensors = []
    beacons = []
    for coord in coords:
        beacons.append((coord[2], coord[3]))
        sensors.append((coord[0], coord[1], abs(coord[0]-coord[2]) + abs(coord[1]-coord[3])))
    beacons = set(beacons)
    blocked = []
    for sensor in sensors:
        if abs(sensor[1] - target) <= sensor[2]:
            radius = sensor[2] - abs(sensor[1] - target)
            blocked.append((sensor[0] - radius, sensor[0] + radius))
    blocked.sort()
    idx = len(blocked) - 1
    while idx > 0:

        if blocked[idx][0] <= blocked[idx-1][1]:

            new = (blocked[idx-1][0], max(blocked[idx-1][1], blocked[idx][1]))
            blocked[idx-1] = new
            blocked.pop(idx)
            blocked.sort()
            idx = len(blocked) - 1
        else:
            idx -= 1
    print(blocked)
    print([(x,y) for (x,y) in beacons if y == target])
    return sum(b-a+1 for (a,b) in blocked) - len([(x,y) for (x,y) in beacons if y == target])

def hard_solution(filename, maximum):
    lines = open(filename).readlines()
    coords = []
    for line in lines:
        x = re.search(input_format, line)
        coords.append( list(int(coord) for coord in x.groups()))
    sensors = []
    beacons = []
    for coord in coords:
        beacons.append((coord[2], coord[3]))
        sensors.append((coord[0], coord[1], abs(coord[0]-coord[2]) + abs(coord[1]-coord[3])))
    beacons = set(beacons)
    for target in range(0, maximum + 1):
        blocked = []
        for sensor in sensors:
            if abs(sensor[1] - target) <= sensor[2]:
                radius = sensor[2] - abs(sensor[1] - target)
                blocked.append((sensor[0] - radius, sensor[0] + radius))
        blocked.sort()
        idx = len(blocked) - 1
        while idx > 0:
            if blocked[idx][0] <= blocked[idx-1][1]:
                new = (blocked[idx-1][0], max(blocked[idx-1][1], blocked[idx][1]))
                blocked[idx-1] = new
                blocked.pop(idx)
                blocked.sort()
                idx = len(blocked) - 1
            else:
                idx -= 1
        if len(blocked) > 1:
            if blocked[1][0] > blocked[0][1] + 1:
                return ((blocked[1][0] + blocked[0][1])//2 * 4000000 + target)
    return "None found"


print("Easy Test: ", easy_solution("test-input", 10))
print("Easy Real: ", easy_solution("input", 2000000))

print("Hard Test: ", hard_solution("test-input", 20))
print("Hard Real: ", hard_solution("input", 4000000))