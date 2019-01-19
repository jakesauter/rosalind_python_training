"""
We will need to consult the monoisotopic table for this
program to access the weighted alphabet
"""

f = open("monoisotopic_table.txt")
raw = f.read()
f.close()

weights = raw.strip().split()

weight_table = dict(zip(weights[::2], [float(x) for x in weights[1::2]]))

"""
Now that we have the weight table we are ready to digest
any string of amino acids and spit out its total mass
"""

prot_str = input().strip()

prot_weight = 0

for x in prot_str:
    prot_weight += weight_table[x]
    
print(round(prot_weight,3))
