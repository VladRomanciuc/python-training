
import string
myString = "This is a string."
print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString)))


firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
print(name)



color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))

def print_rangoli(size):
    alphabet = list(string.ascii_lowercase)
    if size < len(alphabet):
        Line=[]
        for i in range(0, size):
            line = "-".join(alphabet[i:size])
            Line.append((line[::-1]+line[1:]).center(4*size-3, "-"))
        print('\n'.join(Line[:0:-1]+Line))