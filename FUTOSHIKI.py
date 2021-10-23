List = []
n = int(input("Size of puzzle NxN"))
print("Enter Numbers")
for i in range(n):
    List1 = []
    for j in range(n):
        value = int(input("Value -- "))
        List1.append(value)
    List.append(List1)

print(List)

def isNumPresent(List, row, col, num):
    for x in range(n):
        if List[row][x] == num:
            return False
    for x in range(n):
        if List[x][col] == num:
            return False

def solveFutoshiki(List,row,col):
    if(row == n-1 and col == n):
        return True

    if col == n:
        row += 1
        col = 0

    if List[row][col] > 0:
        return solveFutoshiki(List, row, col+1)
    for num in range(1,n+1):
        if isNumPresent(List,row,col,num):
            List[row][col] = num
            if solveFutoshiki(List, row, col+1):
                return True
        List[row][col] = 0
    return False

    def printing(List):
    print("The answer is :")
    for i in range(n):
        for j in range(n):
            print(List[i][j], end = " ")
        print()


    if(solveFutoshiki(List,0,0)):
        printing(List)
        else: 
            print("No solution exists") 



import pygame
pygame.init()
pygame.display.set_caption('FUTOSHIKI')
font = pygame.font.SysFont('comic sans',38)
img = font.render('score :',True,(0,0,0))
running = True
while running:
    screen = pygame.display.set_mode((700,700))
    screen.fill((182, 164, 166))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = false
    for i in range(0,4):
        for j in range(0,4):
            pygame.draw.rect(screen,(215, 207, 219), pygame.Rect(40 + j*180,40 + i*180, 80, 80))
    screen.blit(img, (620, 620))
    pygame.display.flip()
          
            

    
