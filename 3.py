import sys

def main(part):
    f = open("input3.txt", "r")

    sacks = []
    for l in f:
        sacks.append(l.strip())
    #sacks = sacks[:6]
    sum = 0

    if "1" in part:
        for s in sacks:
            l, r = split(s)
            item = [i for i in l if i in r][0]
            sum += prio(item)


    if "2" in part:
        iterable = iter(sacks)
        for a, b, c in zip(iterable, iterable, iterable):
            item = [i for i in a if i in b and i in c][0]
            sum += prio(item)
    print(sum)


def split(a):
    half = len(a)//2
    return a[:half], a[half:]

def prio(c):
    n = ord(c.swapcase())-64
    return n if n < 27 else (n-6)

main(sys.argv[1:])