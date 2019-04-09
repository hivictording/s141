# Author: Victor Ding

import re

string = "Hello world wide web"

patt = re.compile(r'[a-z]+ [a-z]+',flags=re.I)
patt1 = re.compile(r'([a-z]+) ([a-z]+)',flags=re.I)

m = patt.match(string)
m1 = patt1.match(string)

m2 = patt.search(string)
m3 = patt1.search(string)

# print(m.group())
# print(m.group(0))
#
# print(m1.group())
# print(m1.group(0))
# print(m1.group(1))
# print(m1.group(2))

print(m2.group())
print(m2.group(0))
print(m2.groups())
print(m2.groupdict())

print(m3.group())
print(m3.group(0))
print(m3.group(1))
print(m3.group(2))
print(m3.groups())
print(m3.groupdict())

m4 = patt.findall(string)
for i in m4:
    print(i)

m5 = patt1.findall(string)
for i in m5:
    print(i)

m6 = patt.finditer(string)
for i in m6:
    print(i.group())

m7 = patt1.finditer(string)
for i in m7:
    print(i.group())