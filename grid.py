N = 4
def printing(futo_arr):
    for i in range(N):
        for j in range(N):
            print{futo_arr[i][j], end = " " )
    print()

def isSafe(grid, row, col, num):
    for x in range(4):
        if grid[row][x] == num:
            return False
    for x in range(4):
        if grid[x][col] == num:
            return False

def solveFutoshiki(grid,row,col):
    if(row == N-1 and col == N):
        return True


    if col == N:
        row += 1
        col = 1

    if grid[row][col] > 0:
        return solveFutoshiki(grid, row, col+1)
    for num in range(1,N+1):
        if isSafe(grid,row,col,num):
            grid[row][col] = num
            if solveFutoshiki(grid, row, col+1):
                return True
            grid[row][col] = 0
        return False
    
    

