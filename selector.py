## import sys
## print(sys.prefix)

import random

n = int(input('How many time do you wanna get random numbers?: '))

for i in range(n):
    l = random.sample(range(0, 100), 6)
    print(l)
