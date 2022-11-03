import os
import sys
import re

if len(sys.argv) > 2:
    sys.exit("\n!!TOO MANY ARGUMENTS PASSED!!\n\tABORTING\n")

file = sys.argv;

input = open(file[1], "r")

input = input.read()

input = input.upper()

input = input.replace(" ", "")

input = re.sub(r'[^\w\s]', '', input)

input = os.linesep.join([s for s in input.splitlines() if s])

input = input.replace('\n', '')

with open('output.txt', 'w') as f:
    f.write(input)

print("DONE!\n")