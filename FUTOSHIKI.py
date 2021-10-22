# just an example to find the empty cells in the grid
futoshiki = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def findCellNum(futoshiki):
    for x in range(4):
        for y in range(4):
            if futoshiki[x][y] == 0:
                print(x,y)
    return
print(findCellNum(futoshiki))

M = 4

def isPresentRow(grid, row, num):
	for x in range(4):
		if grid[row][x] == num:
			return False
def isPresentCol(grid, col, num):		    
	for x in range(4):
		if grid[x][col] == num:
			return False


def Futoshiki(grid, row, col):
	if (row == M - 1 and col == M):
		return True

	for x in range(4):
                for y in range(4):
                        if x < 4:
                                x++
                        if x = 4:
                                x = 0
                                y++
        
                                

    
