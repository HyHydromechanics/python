shape = 10
i = j = k = 1
put = int(input())
for i in range(0, put):
    for j in range(0, put-1):
        print("*"),
        j += 1
    i += 1
    print("\n")

import random

a = random.randint()