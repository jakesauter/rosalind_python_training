string = input().split()

n = int(string[0])

k = int(string[1])

rabbits = [1]*(n)

for i in range(2, n):

    rabbits[i] = rabbits[i-1] + rabbits[i-2]*k
    
print(rabbits[n-1])
