# Author: Victor Ding

import re

string = 'Hello world wide web 456 789'

patt = re.compile(r'([a-z]+) ([a-z]+)',flags=re.I)

def replace(m):
    print("Function 'replace':",m.group(1),m.group(2),end=' ')

# new_string = patt.sub(r'123',string)
# print(new_string)

new_string = patt.sub(replace,string)
print(new_string)

new_string = patt.subn(replace,string)
# print(type(new_string))
print(new_string)

