import sys
#import math

class Rope:
    def __init__(self, length):
        self.x = 0
        self.y = 0
        self.child = None
        self.hasVisited = set()
        if length > 1:
            self.child = Rope(length-1)

    def move(self,dir,n):
        for i in range(n):
            if dir == "U":
                self.y += 1
            elif dir == "D":
                self.y -= 1
            elif dir == "L":
                self.x -= 1
            elif dir == "R":
                self.x += 1
            if self.child:
                self.child.__drag(self.x, self.y)

    def __drag(self, i, j):
        dx = i - self.x
        dy = j - self.y
        if abs(dx) > 1 or abs(dy) > 1:
            self.x = self.__updateAxis(self.x,dx)
            self.y = self.__updateAxis(self.y,dy)
            
            
            if self.child:
                self.child.__drag(self.x, self.y)
        self.hasVisited.add((self.x, self.y))
    
    def getTailVisited(self):
        if self.child:
            return self.child.getTailVisited()
        return len(self.hasVisited)

    def __updateAxis(self,a,b):
        if b == 0:
            return a
        if b > 0:
            return a + 1
        if b < 0:
            return a - 1

def main(part):
    f = open("input9.txt", "r")

    if "1" in part:
        r = Rope(2)
        for l in f:
            dir, num = l.strip().split()
            r.move(dir,int(num))
            
        print(r.getTailVisited())
    
    if "2" in part:
        r = Rope(10)
        for l in f:
            dir, num = l.strip().split()
            r.move(dir,int(num))
            
        print(r.getTailVisited())


    #original part 1 solution
    '''
    head = [0,0]
    tail = [0,0]

    hasVisited = dict()
    hasVisited[f"{tail[0]},{tail[1]}"] = 1

    count = 0
    for l in f:
        count+=1
        #if count > 150:
        #    break
        dir, num = l.strip().split()
        num = int(num)
        print(l.strip())
        for i in range(num):
            if dir == "U":
                head[1] += 1
            elif dir == "D":
                head[1] -= 1
            elif dir == "L":
                head[0] -= 1
            elif dir == "R":
                head[0] += 1
            
            delta = [(head[0] - tail[0]), head[1] - tail[1]]
            print(head)
            print(tail)
            print(delta)
            if max(delta) > 1 or min(delta) < -1:
                if delta[0] > 0:
                    tail[0] += 1
                if delta[0] < 0:
                    tail[0] -= 1
                if delta[1] > 0:
                    tail[1] += 1
                if delta[1] < 0:
                    tail[1] -= 1
                hasVisited[f"{tail[0]},{tail[1]}"] = 1
            print(tail)
            print("=========")

                
    print(len(hasVisited))
    '''



main(sys.argv[1:])