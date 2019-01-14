"""
A much smarter solution to this problem. The ages list keeps track of 
the rabbits of each age with each of it indices, with the first index
being the amount of rabbits that are 1 month old, the second index
being the amount of rabbits that are two months old and so on. Thus
the total amount of rabbits is the sum of this ages array. An important
note is that the ages array is only as long as the oldest possible age
"""

string = open('rosalind_fibd.txt').readline().strip().split()

n = int(string[0])
m = int(string[1])

ages = [1] + [0]*(m-1)
for i in range(n-1):
    ages = [sum(ages[1:])] + ages[:-1]

print(sum(ages))
