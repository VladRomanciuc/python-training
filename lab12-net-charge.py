# Calculating the Net Charge of Insulin by Using Python Lists and Loops
#12 Assigning variables
lsInsulin = open("lsinsulin-seq-clean.txt", "r").read()

bInsulin = open("binsulin-seq-clean.txt", "r").read()

aInsulin = open("ainsulin-seq-clean.txt", "r").read()

cInsulin = open("cinsulin-seq-clean.txt", "r").read()

preproInsulin = lsInsulin + bInsulin + cInsulin + aInsulin

insulin = bInsulin + aInsulin

#13 Create a new dictionary
pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25,
}
#18  Find all entities from a list using list comprehension
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

#19 Create a variable called pH and initialize it to zero
pH = 0

#20 Create the while loop
while (pH <= 14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    print('{0:.2f}'.format(pH), netCharge)
    pH +=1
    