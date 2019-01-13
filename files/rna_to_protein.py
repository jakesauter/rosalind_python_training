""" Load in the rna codon table into a dictionairy"""

string = input()

f = open("rna_codon_table.txt")

raw = f.read()

f.close()

arr = [x.strip() for x in raw.split(' ') if((x!='') and (x!='\n'))]

d = {}

for x in range(0,len(arr)-1, 2):
    
    d[arr[x]] = arr[x+1]
            

new_string = ''

for x in range(0,len(string),3):
    new_string += d[string[x:x+3]]
    
print(new_string[:-4])
