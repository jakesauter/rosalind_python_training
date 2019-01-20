def rev_comp(pattern):

    rev_comp = []

    for x in pattern:
        if x=='A':
            rev_comp.append('T')
        elif x=='T':
            rev_comp.append('A')
        elif x=='G':
            rev_comp.append('C')
        elif x=='C':
            rev_comp.append('G')

    return ''.join(rev_comp)[::-1]

"""===============MAIN==============="""

"""
First we must obtain the input pattern
"""

f = open('rosalind_revp.txt')
raw = f.read()
f.close()

pattern = ''.join(raw.strip().split()[1:])

"""
Now that we have the input pattern we can work on finding these
'reverse palindrome' sequences between lengths 4 and 12
"""

site_list = []

for l in range(4,12+1): 
    for i in range(len(pattern)-l+1):
        cur_pattern = pattern[i:i+l]
        if(cur_pattern == rev_comp(cur_pattern)):
            site_list.append((i, l))

"""
sort the site list by index 
"""

site_list.sort(key=lambda tup: tup[0])

for tup in site_list:
    print(tup[0]+1, tup[1])
