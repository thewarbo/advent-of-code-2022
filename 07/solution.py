

def create_tree(filename):
    commands = open(filename).read().strip("$ \n").split("\n$ ")
    wd = []
    dirs = {"/"}
    files = {}
    for command in commands:
        if command == "cd /":
            wd = []
        elif command == "cd ..":
            wd.pop()
        elif command[:3] == "cd ":
            wd.append(command[3:])
        elif command[:3] == "ls\n":
            contained = command[3:].split("\n")
            for item in contained:
                if item[:4] == "dir ":
                    dirs.add("/" + "/".join(wd + [item[4:]]) + "/")
                else:
                    size, name = item.split(" ")
                    files["/" + "/".join(wd + [name])] = int(size)

        else:
            print(command[:6])
    return [dirs, files]

def easy_solution(filename):
    dir_sizes = {}
    dirs, files = create_tree(filename)
    for dir in dirs:
        dir_sizes[dir] = sum([files[name] for name in files if name.startswith(dir)])
    return sum(filter(lambda x : x <= 100_000, dir_sizes.values()))

def hard_solution(filename):
    total = 70000000
    update = 30000000
    dir_sizes = {}
    dirs, files = create_tree(filename)
    for dir in dirs:
        dir_sizes[dir] = sum([files[name] for name in files if name.startswith(dir)])
    needed = update - (total - dir_sizes["/"])
    return min((v,k) for k, v in dir_sizes.items() if v > needed)


print(easy_solution("test-input"))
print(easy_solution("input"))
print(hard_solution("test-input"))
print(hard_solution("input"))