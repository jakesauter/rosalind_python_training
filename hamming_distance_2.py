f = open("rosalind_hamm.txt")

a = f.readline()

b = f.readline()

f.close()

print [a!=b for (a, b) in zip(s1, s2)].count(True)
