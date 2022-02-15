lsInsulin = open("lsinsulin-seq-clean.txt", "r").read()

bInsulin = open("binsulin-seq-clean.txt", "r").read()

aInsulin = open("ainsulin-seq-clean.txt", "r").read()

cInsulin = open("cinsulin-seq-clean.txt", "r").read()

#12 Create the first variable in the Python file by entering preproInsulin =
preproInsulin = lsInsulin + bInsulin + cInsulin + aInsulin

#17 merge the results of the smaller insulin groupings into a single variable called insulin.
insulin = bInsulin + aInsulin

#18 Printing "the sequence of human insulin" to console using successive print() commands:
print("The sequence of human preproinsulin: " + preproInsulin)

#23 Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + aInsulin)

# 27 Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  
# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  
# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

#31 example 
molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))