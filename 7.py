import sys

def main(part):
    f = open("input7.txt", "r")
    dirs = {}
    dir_stack = []
    for l in f:
        l = l.strip()
        if "$ cd .." in l:
            dir_stack.pop()
        elif "$ cd" in l:
            dir_name = l[5:]
            if len(dir_stack) > 0:
                dir_name = dir_stack[-1] + "/" + dir_name
            dir_stack.append(dir_name)
            dirs[dir_name] = 0
        elif l[0].isnumeric():
            size = int(l.split()[0])
            for d in dir_stack:
                dirs[d] += size

    sum = 0
    for d in dirs.values():
        if d <= 100000:
            sum += d
    print(sum)

    available = 70000000 - dirs["/"]
    min = 70000000
    dir = 0
    for d in dirs.values():
        space_after_deletion = available + d
        if space_after_deletion >= 30000000 and space_after_deletion <= min:
            min = space_after_deletion
            dir = d
    print(dir)

main(sys.argv[1:])