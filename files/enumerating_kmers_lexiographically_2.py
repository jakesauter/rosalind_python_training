f = open('rosalind_lexf.txt')
raw = f.read()
f.close()

raw = raw.strip().split()

alphabet = raw[0:-1]
length = int(raw[-1])

k_mer = ['']

for l in range(length):
    k_mer =  [i+j for i in alphabet for j in k_mer]
    print(k_mer)

for i in k_mer: 
    print(i)
