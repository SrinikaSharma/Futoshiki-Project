

def findCellNum(futoshiki):
    for x in range(4):
        for y in range(4):
            if futoshiki[x][y] == 0:
                return x,y
    
