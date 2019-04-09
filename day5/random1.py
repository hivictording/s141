# Author: Victor Ding

import random

print(random.random())
print(random.randint(0,9))
check_code = ''

for i in range(10):
    if i == random.randint(0,9):
        temp = chr(random.randint(97,122))
    else:
        temp = random.randint(0,9)

    check_code += str(temp)

print(check_code)