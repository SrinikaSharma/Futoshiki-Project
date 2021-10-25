puzzle = []
n = 4
print("Enter Numbers")
for i in range(n):
    List1 = []
    for j in range(n):
        value = int(input("Value -- "))
        if value > 4:
            print("enter the number in the range 1-4")
            value = int (intput("Value --"))
            List1.append(value)
        else:
            List1.append(value)
    puzzle.append(List1)
print(puzzle)
logic = [
    ["", "", ""],
    ["", "^", "", "v"],
    
    ["", "", ""],
    ["", "", "^", ""],
    
    [">", "", ""],
    ["", "", "", "^"],
    
    ["", "", ""],
    ["", "", "", ""],
]
def puzzle_printer(puzzle, logic):
    for i, l_line in enumerate(logic):
        if (i % 2 == 0):
            line = ""
            for j in range(len(puzzle[0]) - 1):
                line += "{n}{l:1}".format(n=puzzle[i // 2][j], l=l_line[j])
            line += "{}".format(puzzle[i // 2][-1])
            print(line)
        else:
            line = ""
            for l in range(len(l_line)):
                line += "{:1} ".format(l_line[l])
            print(line)

def isNumPresent(puzzle, row, col, num):
    for x in range(n):
        if puzzle[row][x] == num:
            return False
    for x in range(n):
        if puzzle[x][col] == num:
            return False
    if (puzzle[0][1] < puzzle[1][1]):
        return True
    if (puzzle[1][2] < puzzle[2][2]):
        return True
    if (puzzle[2][3] < puzzle[3][3]):
        return True
    if puzzle[0][3] > puzzle[1][3]:
        return True
    if puzzle[2][0] > puzzle[2][1]:
        return True 

def solveFutoshiki(puzzle,row,col):
    if(row == n-1 and col == n):
        return True

    if col == n:
        row += 1
        col = 0

    if puzzle[row][col] > 0:
        return solveFutoshiki(puzzle, row, col+1)
    for num in range(1,n+1):
        if isNumPresent(puzzle,row,col,num):
            puzzle[row][col] = num
            if solveFutoshiki(puzzle, row, col+1):
                return True
        puzzle[row][col] = 0
    return False

def futoshiki_result():
    print("Solution")
    if solveFutoshiki(puzzle,0,0):
        puzzle_printer(puzzle,logic)
    else :
        print("not possible")

futoshiki_result()




            

    
