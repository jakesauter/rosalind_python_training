string = input().strip()
pattern = input().strip()

indices = []

for i in range(len(string)):
    if string[i:].startswith(pattern):
        indices.append(i+1)
        
print(' '.join([str(x) for x in indices]))
