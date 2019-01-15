"""
This program forms the O_3 adjancency list of the overlap
graph of three nucleotide bases
"""

k=3

f = open("rosalind_grph.txt")
raw = f.read()
f.close()

raw = [x.strip() for x in raw.split(">")][1:]

sequences = []
names = []

for block in raw:
    parts = block.split("\n")
    names.append(parts[0])
    seq = ''.join(parts[1:])
    sequences.append(seq)

edges = []

num_seq = len(sequences)

for i in range(num_seq):
    for j in range(num_seq):
        if(sequences[i][-k:] == sequences[j][:k] and 
                        sequences[i] != sequences[j]):
                        
            edges.append([names[i], names[j]])
            
for edge in edges:
    print(edge[0],edge[1])     
