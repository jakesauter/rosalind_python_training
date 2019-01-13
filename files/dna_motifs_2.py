string = input().strip()
pattern = input().strip()

indices = []

r = 0

while r != -1 :
    r = string.find(pattern,r+1)
    indices.append(r+1)

indices = set([str(x) for x in indices])

print(' '.join(indices))
