import csv
import sys
import cs50

if len(sys.argv) != 3:
    sys.exit()

#opening csv file
file1 = open(sys.argv[2])
dna_seq = file1.read()
file2 = open(sys.argv[1])
#dictreader makes a list of dictionary
csv_dictionary = csv.DictReader(file2)
#makes a list of sequences from first seq till however long it actually is
seq = csv_dictionary.fieldnames[1: ]


#counting
dictionary = {}
for seq in seq:
    i = 0
    maximum = 0
    count = 0
    while(i < len(dna_seq) - len(seq)):
        if dna_seq[i: i + len(seq)] == seq:
            count += 1
            if count > maximum:
                maximum = count
            i += len(seq) - 1
        else:
            count = 0
        i += 1
    dictionary[seq] = maximum



#matching
for row in csv_dictionary:
    match = True
    for seq in dictionary:
        if int(row[seq]) != dictionary[seq]:
            match = False
            break
    if match == True:
    #because name is a literal string
        print (row["name"])
        break
if match == False:
    print("No match")

#f.close(file1)
#f.close(file2)
