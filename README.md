TEAM 17

Project Title :  FUTOSHIKI

Description :

Futoshiki is a puzzle game originated in Japan and the word futoshiki (sometimes spelt hutosiki ) means inequality. The puzzle is played on a square grid. The objective of the game is to place the numbers such that each row and column contains only one of each digit.

Rules :

1. In a N x N puzzle the range of #'s must be between 1 and N 
2. No digit is repeated within row or column. No duplicates.
3. Inequality constraints must be honoured: 5 > 4, 5 > 3, or 1 < 4.

Approach:

- We used lists to take input from the user. Incase if the user enters the number which is out of range then it prompts to enter the valid number between the range.
- We fixed the positions of the constraints to make our task easier. 
- Next task is to solve the puzzle.We just defined a function in which we just perform the checking operations based on the rules of futoshiki puzzle i.e,row checking and column checking,constraints condition checking.
- Number will be assigned to the cell if all the above conditions are satisfied.
- To print the puzzle we used format function to concatenate numbers with the strings.
- if the input given by the user is not sufficient to solve the puzzle it displays "not possible".




 














