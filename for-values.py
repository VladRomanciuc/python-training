
#for logic
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n=5

for i in list:
    a=n*i
    print(a)

################################################################

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

#iterate each one from the array
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))

