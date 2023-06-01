import random
import keyboard

# Function to get a random number between 1 and 6
def ranGen():
    return random.randint(1,6)

# Build a dice matrix to store data
def matRix(num):
    # initialize the matrix 
    m=[[" " for i in range(0,15)] for j in range(0,7)]
    ## Loop the matrix
    for x in range(len(m)):
        for y in range(len(m[x])):
            ###Draw the borders
            if x==0:
                m[x][y] = "'" 
            if x ==6:
                m[x][y] = "."
            if y == 0 or y ==14:
                m[x][y]=":"
                #### Dice value checker
                if num == 1:
                    m[3][7] = "o"
                if num == 2:
                    m[2][9] = "o"
                    m[4][5] = "o"
                if num == 3:
                    m[1][11] = "o"
                    m[3][7] = "o"
                    m[5][3] = "o"
                if num == 4:
                    m[1][3] = "o"
                    m[1][11] = "o"
                    m[5][3] = "o"
                    m[5][11] = "o"
                if num == 5:
                    m[1][3] = "o"
                    m[1][11] = "o"
                    m[3][7] = "o"
                    m[5][3] = "o"
                    m[5][11] = "o"
                if num == 6:
                    m[1][3] = "o"
                    m[1][11] = "o"
                    m[3][3] = "o"
                    m[3][11] = "o"
                    m[5][3] = "o"
                    m[5][11] = "o"
    return m
#Print the matrix row by row
def pMatrix(m):
    for x in range(len(m)):
        row=""
        for y in range(len(m[x])):
            row += m[x][y]
        print(row)        

#Main p for play or e for exit
print("press #p to play or #e to exit.")
while True:
    if keyboard.is_pressed("p"):
        num = ranGen()
        pMatrix(matRix(num))
        print("Your luky number is: ", num)
    if keyboard.is_pressed("e"):
        break
