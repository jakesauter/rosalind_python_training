string = input()

num_a = len([x for x in string if x=='A'])

num_c = len([x for x in string if x=='C'])

num_g = len([x for x in string if x=='G'])

num_t = len([x for x in string if x=='T'])


print(num_a, num_c, num_g, num_t)
