puzzle = []
n = int(input("Size of puzzle NxN"))
print("Enter Numbers")
for i in range(n):
    List1 = []
    for j in range(n):
        value = int(input("Value -- "))
        List1.append(value)
    puzzle.append(List1)

def isNumPresent(List, row, col, num):
    for x in range(n):
        if List[row][x] == num:
            return False
    for x in range(n):
        if List[x][col] == num:
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
            List[row][col] = num
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



import pygame
pygame.init()
pygame.display.set_caption('FUTOSHIKI')
running = True
while running:
    screen = pygame.display.set_mode((600,600))
    screen.fill((182, 164, 166))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(0,4):
        for j in range(0,4):
            pygame.draw.rect(screen,(215, 207, 219), pygame.Rect(66.6 + j*133.2,66.6 + i*133.2, 66.6, 66.6))
    pygame.display.flip()
          
            

    
