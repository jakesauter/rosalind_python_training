dnafile = open('rosalind_gc.txt')

raw = dnafile.read()

d = {}

for block in raw.split(">")[1:]:

    parts = block.split("\n")
    name = parts[0]
    seq = ''.join(parts[1:])
    gc = 100 * ( seq.count("G") + seq.count("C") ) / float(len(seq))
    d[gc] = name

print(d[max(d)])
print(max(d))
