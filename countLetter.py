import sys
from collections import Counter
from string import ascii_uppercase

file = sys.argv;

if len(sys.argv) > 2:
    sys.exit("\n!!TOO MANY ARGUMENTS PASSED!!\n\tABORTING\n")

count = []
input = open(file[1], "r")

input = input.read()
l = len(input)

for i in range (0, l):
    count.append(input[i])

c = Counter(count)

temp = ascii_uppercase

alph = []

for i in temp:
    alph.append(i)

i= 0
for e in alph:
    print(alph[i] + ': ', c[e])
    i+=1


#   Thought I needed to sort, I was wrong. I keep him around because sorting is cool
#for i in range(0, l):
#    for j in range(0, l):
#        if count[i] < count[j]:
#            count[i], count[j] = count[j], count[i]
#j = ""