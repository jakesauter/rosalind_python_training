"""
A script calculating the longest commong substring in a 
list of given strings
"""

f = open("rosalind_lcsm.txt")
raw = f.read()
f.close()

raw = [x.strip() for x in raw.split('>')[1:]]

sequences = []

for block in raw:
    sequences.append(''.join(block.split("\n")[1:]))
    
"""
Now that we have all of the sequences in an array we can 
work to find the longest common substring

We will start with the size of the strings and work our
way down until we find the longest common substring between
all of the sequences
"""

def shortest_common_substring(sequences):

    """
    We will check if all of the substrings of the first 
    sequence are contained in all of the other sequences
    """

    seq_len = len(sequences[0])
    min_seq_len = min([len(x) for x in sequences])

    for size in reversed(range(1, min_seq_len+1)):
        for i in range(seq_len-size+1):
            #print("checking if sequence: " + sequences[0][i:i+size] + \
            #        " is in all of the sequences")
            if(all([sequences[0][i:i+size] in x for x in sequences])):
                return(sequences[0][i:i+size])

print(shortest_common_substring(sequences))            



