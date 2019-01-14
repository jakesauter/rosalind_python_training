string = open('rosalind_fibd.txt').readline().strip().split()

n = int(string[0])
m = int(string[1])

little = [0]*(n)
big = [0] * n

little[0], little[1] = 1,0
big[0], big[1] = 0,1

for i in range(2, n):
    little[i] = big[i-1]
    big[i] = little[i-1] + big[i-1] - little[i-m]
     
print([x+y for (x,y) in zip(little,big)][-1])
