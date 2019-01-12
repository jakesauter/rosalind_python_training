"""
Program to calcuate the probability of an offspring
of two organisms carraying a dominatant allele, given
hd homozygus dominaant, h heterozygus and hr homozygyus
recessive invidivuals in the popualation that can all mate
with eachother

hd, h, hr

hd-hd = 1

hd-h = 1

hd-hr = 1

h-h = .75

h-hr = .5

hr-hr = 0
"""

import math

hd,h,hr = [int(x) for x in input().strip().split()]

total = hd + h + hr

p = [0]*9

p[0] = ((hd/total)*((hd-1)/(total-1)))
p[1] = ((hd/total)*(h/(total-1))) 
p[2] = ((hd/total)*(hr/(total-1)))
p[3] = ((h/total)*(hd/(total-1)))
p[4] = ((h/total)*((h-1)/(total-1))*(.75))
p[5] = ((h/total)*(hr/(total-1))*(.5))
p[6] = ((hr/total)*(hd/(total-1)))
p[7] = (((hr/total)*(h/(total-1)))*.5)
p[8] =  (((hr/total)*((hr-1)/(total-1)))*0)

prob = sum(p)

print(prob)
















