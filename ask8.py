#askhsh8

import random

rand_numbers=[]
for i in range(30):
       rand_numbers.append(random.randint(-30,30))

print rand_numbers

found=0
for i in rand_numbers:
    for j in rand_numbers:
        for k in rand_numbers:
            if(i+j+k == 0):
                found = 1
                print i, "\t", j, "\t", k

if(found==0):
    print "de vrethike 3ada me athroisma 0"