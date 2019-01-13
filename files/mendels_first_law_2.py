"""
much better version of mendel's first law program using 
combinatorics as opposed to simple probabilities
"""

hd,h,hr = [int(x) for x in input().strip().split()]

"""
Total Number of possibilities is N * (N-1)
"""

total = hd+h+hr

total *= (total-1)

"""
We will calculate the probability of a recessive allele
combination and take the compliment
"""

prob = 1 - ((h*hr) + (.25*h*(h-1)) + (hr*(hr-1)))/total

print(prob)
