import csv
import random
import keyboard

#Load word data from file
with open('files/words.txt') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=' ')
    data = []
    lineCount = 0
    for row in csvReader:
                f'{" ".join(row)}'
                lineCount += 1
                data.append(row)
#Get a randon number to play the game
def ranWord():
    word = str(data[random.randint(0, len(data)-1)])
    w = word.removeprefix("['").removesuffix("']")
    return w

#Match the word
def wordMatcher(w):
    step = 1
    step2 = len(w) * 12
    score = 0
    
    res = "*" * len(w)
    wordBoard(res)
    while w != res and step2 >= 1:
        letter = str(input("Your letter: "))
        
        for x in range(0, len(w)):
            if w[x] == letter and w[x] != res[x]:
                res = res[:x] + w[x] + res[x + 1:]
                step += (len(w)-1)
                #print(res[x], x)
                #print(w[x], x)
                #print("Step1:", step)
            if w[x] != letter:
                step2 -=1   
                #print("Step2: ", step2)
            if step2 < 1:
                #print("You lost")
                break  
        wordBoard(res)
    score = step2+step
    if score > len(w)*12+1:
        score = len(w)*12+1
    print("The word is " + "'"+ w + "'." + "Your score is: " + str(score) + " from max score: " + str(len(w)*12+1))
    return res, score
    

#draw the word board
def wordBoard(w):   
    #print(len(w))
    #print(w)
    m=[[" " for i in range(0,3*len(w)+1)] for j in range(0,3)]
    for x in range(len(m)):
        for y in range(len(m[x])):
            if x==0:
                m[x][y] = "'" 

            if x == 1 and y > 0 and y < 3*len(w):
                if y % 3 == 1:
                    m[x][y] = w[y//3]
            if x==2:
                m[x][y] = "."
            if y == 0 or y == 3*len(w):
                m[x][y]=":"
            
    #print matrix
    for x in range(len(m)):
        row=""
        for y in range(len(m[x])):
            row += m[x][y]
        print(row)

    return m

#      O    O |
#     /|\  /|\
#     / \  / \
#      O_   O_|
#     \|/  |^|
#     / \  / \
#drawing hangman
def hangman(w, score):
    max_score = len(w) * 12 +1
    #print("Max score: ", max_score)
    n = int(len(w)//2-1)
    if score > (max_score - max_score/4):
        print(" "*n+" O "+" "*n+"\n" + " "*n+"/|\\"+" "*n+"\n" + " "*n+"/ \\"+" "*n+"\n" )
        print("Best performers")
    if score > (max_score - max_score/3) and score < (max_score - max_score/4):
        print(" "*n+" O |"+" "*(n-1)+"\n" + " "*n+"/|\\"+" "*n+"\n" + " "*n+"/ \\"+" "*n+"\n" )
        print("Can be better")
    if score > (max_score - max_score/2) and score < (max_score - max_score/3):
        print(" "*n+" O_"+" "*n+"\n" + " "*n+"\|/"+" "*n+"\n" + " "*n+"/ \\"+" "*n+"\n" )
        print("Almost there")
    if score < (max_score - max_score/2) and score >= 1:
        print(" "*n+" O_|"+" "*(n-1)+"\n" + " "*n+"|^|"+" "*n+"\n" + " "*n+"/ \\"+" "*n+"\n" )
        print("Better luck next time")

##main
print("Let`s start the game...")
w =ranWord()
#print(w)
word, score = wordMatcher(w)

hangman(word, score)
print("############################################")
 
        
