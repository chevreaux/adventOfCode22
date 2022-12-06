import sys

def main(part):
    f = open("input2.txt", "r")

    rounds = []
    moves = {
        'X' : {"score": 1, 'A': 3, 'B': 0, 'C': 6},
        'Y' : {"score": 2, 'A': 6, 'B':3, 'C':0},
        'Z' : {"score": 3, 'A':0, 'B':6, 'C':3}
        }
    if "2" in part:
        moves = {
            'X' : {"score": 0, 'A': 3, 'B': 1, 'C': 2},
            'Y' : {"score": 3, 'A': 1, 'B':2, 'C':3},
            'Z' : {"score": 6, 'A':2, 'B':3, 'C':1}
            }
    score = 0

    for l in f:
        if len(l.strip()) == 3:
            rounds.append((l[0],l[2]))
    
    for r in rounds:
        score += moves[r[1]]["score"] + moves[r[1]][r[0]]
        
    print(score)


main(sys.argv[1:])