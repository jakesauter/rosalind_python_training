import math

"""
Simple function to determing if the part is contained
in all sequences in the array arr
"""
def substring_in_all(arr, part):
  for dna in arr:
    if part not in dna:
      return False
  return True
  
"""
Function to determine if there is a shared substring
of length "length" between all of the elements of the
array arr
"""
def common_substring(arr, length):
  first = arr[0]
  for i in range(len(first)-length+1):
    part = first[i:i+length]
    if substring_in_all(arr, part):
      return part
  return ""

"""
Binary search master function, essentailly a binary search
of the list of possible subtring lengths with the check function
being a shared common substring of that length
e.g. [0 1 2 3 4 5 6 7 8], we first try a substring of length 4, 
if there is a substring of length 4 we try to find a substring
of length 6, if there is not a substring of length 4 we try a 
substring of length 2
"""
def longest_common_substring(arr):
  left = 0; right = len(arr[0])

  while left+1 < right:
    mid = math.floor((left+right) / 2)
    if common_substring(arr, mid)!="":
      left=mid
    else:
      right=mid

  return common_substring(arr, left)
  
"""====================================================="""

f = open("rosalind_lcsm.txt")
raw = f.read()
f.close()

raw = [x.strip() for x in raw.split('>')[1:]]

sequences = []

for block in raw:
    sequences.append(''.join(block.split("\n")[1:]))
    
print(longest_common_substring(sequences))
