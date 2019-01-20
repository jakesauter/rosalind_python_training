from itertools import product

"""
Here I have learned about a Cartesian Product, being a 
product of two sets, which is the same thing as 
permtuations with replacement

This is also very handy as it will generate the permutations
in lexigraphical order, so no further sorting will be needed
"""

f = open('rosalind_lexf.txt')
raw = f.read()
f.close()

raw = raw.strip().split()

characters = raw[0:-1]
length = int(raw[-1])

perms = [x for x in product(characters, repeat=length)]

for perm in perms: 
    print(' '.join(perm))
