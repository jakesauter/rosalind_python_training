import re

"""
We must first begin by taking in the FASTA formated
sequence followed by the identified introns
"""

f = open('rosalind_splc.txt')
raw = f.read()
f.close()

blocks = raw.strip().split('>')[1:]

"""
The first block is the sequence
"""

sequence = ''.join(blocks[0].strip().split()[1:])

introns = []

for block in blocks[1:]:
    introns.append(''.join(block.strip().split()[1:]))
    
"""
Now all we must do is remove the introns from the DNA (splicing)
and trascribe the DNA into RNA by replacing T with U
"""

for intron in introns:
    sequence = sequence.replace(intron, '')
    
sequence = sequence.replace('T','U')
    
"""
Now we are going to need the RNA to Amino table to translate
"""

f = open('rna_to_protein_translation_table.txt')
raw = f.read()
f.close()

raw = raw.strip().split()

table = dict(zip(raw[::2], raw[1::2]))

protein = []

for i in range(0,len(sequence)-3+1,3):
    protein.append(table[sequence[i:i+3]])
    
print(''.join(protein[:-1]))
