import csv

#declare an empty list
sequence = []

#read .csv data and add into my preproinsulin
with open('preproinsulin-seq.txt') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=' ')
    row = []
    lineCount = 0
    for data in csvReader:
                print(f'{" ".join(data)}')
                lineCount += 1
                row.append(data)

sequence.append(row[1]+row[2])

#filter out          
preproinsulin = [x for x in sequence[0] if x != "ORIGIN" and x != "1" and x != "61" and x != "//" and x != '']

print(preproinsulin)

#transform in a string
cleanData = ''.join(preproinsulin) 
print("NEEEEEW", cleanData)

#save the clean file
textfile = open("preproinsulin-seq-clean.txt", "w")
for y in cleanData:
    textfile.write(y.lower())
textfile.close()

#20. Confirm that the file has 110 characters of lowercase letters
with open('preproinsulin-seq-clean.txt') as csvFile:
    workingFile = csv.reader(csvFile)
    for data in workingFile:
        print("Step 20:", len(data[0]), "characters.", "Lowercase:", data[0].islower())

#22. In lsinsulin-seq-clean.txt, save amino acids 1–24. 
        lsinsulin = open("lsinsulin-seq-clean.txt", "w")
        for y in data:
            lsinsulin.write(y[0:24])
            print(y[0:24])
            lsinsulin.close()
#Verify that your file has 24 characters.
            with open('lsinsulin-seq-clean.txt') as csvFile:
                workingFile22 = csv.reader(csvFile)
                for data in workingFile22:
                    print("Step 22:", len(data[0]), "characters.")
#24.In binsulin-seq-clean.txt, save amino acids 25–54. 
            binsulin = open("binsulin-seq-clean.txt", "w")
            binsulin.write(y[24:54])
            print(y[24:54])
            binsulin.close()
# Verify that your file has 30 characters.
            with open('binsulin-seq-clean.txt') as csvFile:
                workingFile24 = csv.reader(csvFile)
                for data in workingFile24:
                    print("Step 24:", len(data[0]), "characters.")
#26. In cinsulin-seq-clean.txt, save amino acids 55–89. 
            cinsulin = open("cinsulin-seq-clean.txt", "w")
            cinsulin.write(y[54:89])
            print(y[54:89])
            cinsulin.close()
# Verify that your file has 35 characters.
            with open('cinsulin-seq-clean.txt') as csvFile:
                workingFile26 = csv.reader(csvFile)
                for data in workingFile26:
                    print("Step 26:", len(data[0]), "characters.")
#28. In ainsulin-seq-clean.txt, save amino acids 90–110. 
            ainsulin = open("ainsulin-seq-clean.txt", "w")
            ainsulin.write(y[89:110])
            print(y[89:110])
            ainsulin.close()
# Verify that your file has 21 characters.
            with open('ainsulin-seq-clean.txt') as csvFile:
                workingFile28 = csv.reader(csvFile)
                for data in workingFile28:
                    print("Step 28:", len(data[0]), "characters.")