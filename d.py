import csv
#f = open("find_words.txt", "r")
r=csv.reader(open('french_dictionary.csv', 'r'))
#for x in f:
 # print(x)
d = {}
for row in r:
    key, value = row
    d[key] = value
    #print(value)
    #print(row)

oldwords = str(d.keys())
newwords = str(d.values())
#print(newwords)
#print(oldwords)

with open('new.txt', 'wt') as outfile:
    with open('find_words.txt', 'rt') as infile:
        for line in infile:
            outfile.write(line.replace(newwords,oldwords))
            
