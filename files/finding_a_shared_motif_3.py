def longestCommon(seqs):
  shortest = min(seqs, key=len)
  for length in xrange(len(shortest), 0, -1):
    for start in xrange(len(shortest) - length + 1):
      sub = shortest[start:start+length]
      if all(seq.find(sub) >= 0 for seq in seqs):
        return sub
  return ""
  
"""====================================================="""

f = open("input.txt")
raw = f.read()
f.close()

raw = [x.strip() for x in raw.split('>')[1:]]

sequences = []

for block in raw:
    sequences.append(''.join(block.split("\n")[1:]))
    
print(longest_common_substring(sequences))
