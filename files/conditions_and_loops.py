bounds = input().split()

bounds = [int(x) for x in bounds]

total_sum = 0

# if the starting bound is not odd, make it odd

if(bounds[0] % 2 == 0): bounds[0] += 1

print(bounds[0], bounds[1])

for i in range(bounds[0], bounds[1]+1, 2):
  
  total_sum += i


print(total_sum)
