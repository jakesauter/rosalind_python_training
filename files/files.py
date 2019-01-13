new_file = open("new_file.txt", 'w+')

with open("rosalind_ini5.txt") as f:
  
  for line in f:  

    new_file.write(f.readline())

new_file.close()
