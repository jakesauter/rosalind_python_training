string = input().split()

words = set(string)

words_dict = {}

for word in words:

  words_dict[word] = string.count(word)


for k,v in words_dict.items():

   print(k,v)
