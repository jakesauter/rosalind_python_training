f = open("rosalind_hamm.txt")

a = f.readline()
b= f.readline()

f.close()

count=0

for i in range(0, len(a)):

    if(a[i] != b[i]): count += 1
        
print(count)
