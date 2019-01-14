raw = open("input.txt").read()


"""
First we will form a 2d array of all of the provided 
sequences
"""

sequences = []

raw = [x.strip() for x in raw.split(">")][1:]




for block in raw:

    parts = block.split("\n")
    seq = ''.join(parts[1:])
    sequences.append(seq)
    
"""
Store the number of columns needed later for the profile
for more efficient memory allocation
"""
ncols = len(seq)
    
"""
Now we will generate the profile of the group of sequneces 
"""

profile = [[0]*ncols for i in range(4)]

bases = "ACGT"

for base in range(4):
    for col in range(ncols):
        profile[base][col] = [x[col] for x in sequences].count(bases[base])
        

    
"""
Now we can finally generate the consensus
"""

consensus = [0]*ncols

for col in range(ncols):
    cur = [x[col] for x in profile]
    index = cur.index(max(cur))
    consensus[col] = bases[index]
    
print(''.join(consensus))

for i in range(4):
    print(bases[i] + ': ' + ' '.join([str(x) for x in profile[i]]))
