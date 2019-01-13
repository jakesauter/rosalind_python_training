"""
We will make use of regular expressions to produce 
a list of indexes of matches
"""

import re

string = input().strip()
pattern = input().strip()

"""
Since we need to locate overlapping strings we need to use 
the regex feature of re.finditer('(?=tt)', 'ttt') -- [0,1]
called a "lookahead assertion"
"""

x = [int(m.start())+1 for m in re.finditer('(?='+pattern+')', string)]

x = [str(x) for x in x]

print(' '.join(x))
