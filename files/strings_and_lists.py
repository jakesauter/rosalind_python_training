string  = input()
input_nums = input()

input_nums = input_nums.split()

input_nums = [int(x) for x in input_nums]

print(string[input_nums[0]:input_nums[1]+1] + " " + string[input_nums[2]:input_nums[3]+1])
