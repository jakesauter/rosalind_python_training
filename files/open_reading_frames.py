"""
First we will need the rna to protein translation
table
"""

f = open('rna_to_protein_translation_table.txt')
raw = f.read()
f.close()

string = raw.strip().split()

d = dict(zip(string[::2], string[1::2]))

"""
Read string from FASTA format
"""

f = open("rosalind_orf.txt")
raw = f.read()
f.close()

string = ''.join([x.strip() for x in raw.split()][1:])
str_len = len(string)

"""
We will transcribe this DNA into RNA so that our previously made
table can be used
"""

string = string.replace('T', 'U')


"""
We will have to search for start-stop codon encapsulated
chunks of this original string and the compliment of the
string
"""

"""
While writing this code I got curious if it is faster to keep
appending to a string or to form a list then join at the end,
while researching this I found the 'timeit' tool that can 
be used the following way

>>> import timeit
>>> timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
"""

compliment = [0]*str_len

for i in range(str_len):
    if(string[i] == 'A'):
        compliment[i] = 'U'
    elif(string[i] == 'U'):
        compliment[i] = 'A'
    elif(string[i] == 'G'):
        compliment[i] = 'C'
    elif(string[i] == 'C'):
        compliment[i] = 'G'
        
compliment = ''.join(compliment)[::-1]
    
"""
Now we have to search for start-stop codon ecapsualted strings
in the DNA content
"""

proteins = []

for seq in [string,compliment]:
    for offset in range(0,3):
        sequences = [d[seq[i:i+3]] for i in range(offset,str_len-2,3)]
        
        """M = Start"""
        start = [i for i,x in enumerate(sequences) if x=='M']
        stop = [i for i,x in enumerate(sequences) if x=='Stop']
            
        """
        Only keep the starts less than the stop
        """
        
        for x in start:
            try: 
                stop_index = min([y for y in stop if y > x])
            except:
                continue
                
            proteins.append(''.join(sequences[x:stop_index]))
   

for protein in set(proteins):
    print(protein)    
