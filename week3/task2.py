#task 2

import random
count = 0
num = None
while num != 0:
    num = random.randint (0, 10)
    count = count + 1
    print (num)
    if num == 7:
        print (" Lucky 7! ")
print("it has generated", count, "numbers")
