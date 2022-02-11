myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[2] = "orange"
print(myFruitList)


myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])


myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])


#Mini DB inside the code

#list
var1 = []
#tuple
const1 = ("key1", "key2", "key3", "key4")
#dictionary
dict1 = {
    const1[0]: 111111,
    const1[1]: 555555,
    const1[2]: 666666,
    const1[3]: True,
}
#add to list only you need
var1.append(dict1[const1[1]])
var1.append(dict1[const1[3]])
#print list
print(var1[0], var1[1])