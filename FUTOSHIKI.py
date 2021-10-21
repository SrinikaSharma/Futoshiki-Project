# just an example to find the empty cells in the grid
futoshiki = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def findCellNum(futoshiki):
    for x in range(4):
        for y in range(4):
            if futoshiki[x][y] == 0:
                print(x,y)
    return
print(findCellNum(futoshiki))

    
