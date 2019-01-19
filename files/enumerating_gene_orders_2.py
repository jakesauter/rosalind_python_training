"""
Recursive version just to build understanding
"""
def permutation(lst):

    """If the list is empty then there are no permutations"""
    if(len(lst)==0):
        return []
    
    """If there is only one item in the list then there is
        only one possible permutation"""
    if(len(lst)==1):
        return [lst]
        
    """More than one item in the list"""
    
    """Empty list that we will store the current perm in"""
    l = []
    
    """Iterate through the input list and calculate the perms"""
    for i in range(len(lst)):
        m = lst[i]
        
        """Extract m=lst[i] from the list and deal with 
           the remaining list portion"""
        remlst = lst[:i] + lst[i+1:]
        
        """Generate all permutations where m is the first element"""
        for p in permutation(remlst):
            l.append([m]+p)

    return l


"""=================MAIN================="""

import math

n = int(input().strip())

data = list(range(1,n+1))

for p in permutation(data):
    print(' '.join([str(x) for x in p]))



