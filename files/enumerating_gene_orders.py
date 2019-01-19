import math
from itertools import permutations

n = int(input().strip())

nperms = math.factorial(n) 

perms = list(permutations(range(1,n+1)))

print(nperms)

for perm in perms:
    print(' '.join([str(x) for x in perm]))
