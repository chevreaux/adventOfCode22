import sys

def main(part):
    f = open("input5.txt", "r")
    rows = []
    moves = []
    for l in f:
        ls = l.strip()
        if ls == "":
            continue
        if l.startswith("move"):
            moves.append(processMove(ls))
        elif "[" in l:
            rows.append(l)
    stacks = processRows(rows)
    for m in moves:
        stacks[m[1]], stacks[m[2]] = move(m[0], stacks[m[1]], stacks[m[2]], part)


    for s in stacks:
        print(s[-1],end="")

def processMove(move):
    m = move.split(' ')
    return (int(m[1]), int(m[3])-1, int(m[5])-1)

def processRows(rows):
    boxCount = (len(rows[0]) + 1) // 4
    stacks = [[] for _ in range(boxCount)]
    rows.reverse()
    for r in rows:
        for i in range(boxCount):
            j = i * 4 + 1
            if r[j] != " ":
                stacks[i].append(r[j])
    return stacks


def move (count, src, dest, part):
    hold = src[-count:]
    if "2" not in part:
        hold.reverse()
    dest.extend(hold)
    src = src[:-count]
    return src, dest
    
    

main(sys.argv[1:])