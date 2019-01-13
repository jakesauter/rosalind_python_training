f = open("rosalind_hamm.txt")

s1 = f.readline()

s2 = f.readline()

f.close()

print([a!=b for (a, b) in zip(s1, s2)].count(True))
