from time import sleep
from random import randint
        
def checkRowCol(table, row, col ,num):
    # Check row and column
    for i in range(9):
        if num == table[row][i]:
            print("\nThere are the same number in the row.\n")
            return 0 # row same case
        elif num == table[i][col]:
            print("\nThere are the same number in the column.\n")
            return 0 # column same case
        
    # if no same number in row and column
    if table[row][col] == 0:
        table[row][col] = num
        print("Added!!!")
        return 0
    else:
        print("\nThere is a number already.\n")
        return 0

# start setup   
table = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]

for i in range(30):
    r, c, n = [randint(0,8), randint(0,8), randint(0,9)]
    table[r][c] = n
    
# table game over test
# table = [[5,3,4,6,7,8,9,1,2],
#          [6,7,2,1,9,5,3,4,8],
#          [1,9,8,3,4,2,5,6,7],
#          [8,5,9,7,6,1,4,2,3],
#          [4,2,6,8,5,3,7,9,1],
#          [7,1,3,9,2,4,8,5,6],
#          [9,6,1,5,3,7,2,8,4],
#          [2,8,7,4,1,9,6,3,5],
#          [3,4,5,2,8,6,1,7,9]]

while True:
    sleep(2)
    print(*table, sep="\n")
    try:
        row = int(input("\nSelect the row (1-9): "))
        col = int(input("Select the column (1-9): "))
        num = int(input("Enter a number (1-9): "))
    except TypeError:
        print("\nPlease, enter a number only 1-9.\n")
    else:
        if not(row >= 1 and row <= 9):
            print("\nThe row is out of range(1-9).\n")
            continue
        elif not(col >= 1 and col <= 9):
            print("\nThe column is out of range(1-9).\n")
            continue
        elif not(num >= 1 and num <= 9):
            print("\nThe number is out of range(1-9).\n")
            continue
        else:
            row -= 1
            col -= 1 
            checkRowCol(table, row, col, num)
            flag = 81 # 9x9
            for i in range(9):
                for j in range(9):
                    if table[i][j] != 0:
                        flag -= 1
            if flag == 0:
                print("\n Game Over!!! \n")
                break