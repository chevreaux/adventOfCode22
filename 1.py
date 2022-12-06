def main():
    f = open("input1.txt", "r")

    top3 = [0,0,0]
    s = 0

    while True:
        line = f.readline()
        if not line or line == "\n":
            if s > top3[0]:
                top3 = compare(top3, s)
            print(f"Total: {s}\n")
            s = 0
            if not line:
                break
            continue
        print(line, end="")
        s += int(line)

    f.close()
    print(f"Top3: {sum(top3)}")


def compare(top3, n):
    top3.append(n)
    top3.sort()
    return top3[1:]


main()