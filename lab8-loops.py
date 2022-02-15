#import random generator
import random

#inform about rules
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#declare variable number and assign a random number between 1 and 10
number = random.randint(1,10)

#declare an operation/trigger variable boolean type
isGuessRight = False

#start the loop by asking to input a random number, checking if there is a match, if no looping
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))



#difference
print("Count to 10!")

for x in range (0, 11):
    print(x)