import sys

def main(part):
    f = open("input4.txt", "r")

    pairs = []
    for l in f:
        a, b = l.strip().split(",")
        a1, a2 = a.split("-")
        b1, b2 = b.split("-")
        pairs.append(((int(a1),int(a2)),(int(b1),int(b2))))
    #pairs = pairs[:6]
    print(pairs)
    sum = 0
    if "1" in part:
        for p in pairs:
            if (p[0][0] >= p[1][0] and p[0][1] <= p[1][1]) or (p[0][0] <= p[1][0] and p[0][1] >= p[1][1]):
                sum += 1

    if "2" in part:
        for p in pairs:
            if (p[0][0] >= p[1][0] and p[0][0] <= p[1][1]) or (p[1][0] >= p[0][0] and p[1][0] <= p[0][1]):
                sum += 1
    print(sum)
    
main(sys.argv[1:])