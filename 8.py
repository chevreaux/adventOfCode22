import sys

def main(part):
    f = open("input8.txt", "r")
    grid = []
    viewFromNorth = [] # highest tree seen yet in column i
    viewFromSouth = []
    visibilityGrid = [] #keep track of visible trees on first pass to avoid double counting
    treeSum = 0

    #parse data and do a first pass for height checking at the same time
    for l in f:
        r = l.strip()
        row = []
        visibilityRow = [] 
        viewFromWest = -1 # highest tree seen yet in row from the west
        
        if len(viewFromNorth) == 0: #init view lists
            viewFromNorth = [-1 for _ in range(len(r))]
        if len(viewFromSouth) == 0:
            viewFromSouth = [-1 for _ in range(len(r))]
    
        for i, c in enumerate(r):
            h = int(c) #height of tree
            row.append(h)
            isVisible = False

            if h > viewFromNorth[i]:
                viewFromNorth[i] = h
                isVisible = True 
            if h > viewFromWest:
                viewFromWest = h
                isVisible = True

            if isVisible:
                visibilityRow.append(1)
                treeSum += 1
            else:
                visibilityRow.append(0)
        grid.append(row)
        visibilityGrid.append(visibilityRow)


    #second pass for height checking
    for j, r in reversed(list(enumerate(grid))):
        viewFromEast = -1 # highest tree seen yet in row from the east
        for i, c in reversed(list(enumerate(r))):
            h = int(c) #height of tree at (i,j)
            isVisible = False
            if h > viewFromSouth[i]:
                viewFromSouth[i] = h
                isVisible = True 
            if h > viewFromEast:
                viewFromEast = h
                isVisible = True
            if isVisible and visibilityGrid[j][i] == 0:
                treeSum += 1

    print(treeSum)



    #part 2

    max = 0
    for i, row in enumerate(grid):
        if i == 0 or i == len(grid)-1: continue
        for j, col in enumerate(row):
            if j == 0 or j == len(row)-1: continue
            
            #check north
            n = 1
            while i-n > 0:
                if grid[i-n][j] < col:
                    n += 1
                if grid[i-n][j] >= col:
                    break

            #check south
            s = 1
            while i+s < len(grid)-1:
                if grid[i+s][j] < col:
                    s += 1
                if grid[i+s][j] >= col:
                    break

            #check west
            w = 1
            while j-w > 0:
                if grid[i][j-w] < col:
                    w += 1
                if grid[i][j-w] >= col:
                    break

            #check east
            e = 1
            while j+e < len(row)-1:
                if grid[i][j+e] < col:
                    e += 1
                if grid[i][j+e] >= col:
                    break
            score = n * s * w * e
            
            if score > max:
                max = score

    print(max)

    

                
            



main(sys.argv[1:])