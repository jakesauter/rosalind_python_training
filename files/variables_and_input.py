from math import sqrt 

args = input().split()

float_args = [int(x) for x in args]

a,b = float_args

print(a**2 + b**2)
