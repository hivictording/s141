# Author: Victor Ding

import re

string="Cast:Tom Cruise,Director:David Finch"

# patt = "[a-zA-Z]+\s[a-zA-Z]+"
# m=re.findall(patt,string)
# print (m)

# compile: 说明：将正则表达式转换为模式对象，实现更有效率的匹配，因为其他的函数会在内部进行转换。
# patt = re.compile(r'[a-zA-Z]+\s[a-zA-Z]+')
patt = re.compile(r'(?P<Actor>[A-Za-z]+)')

# match:说明：在给定的字符串的开头匹配正则表达式。
# m = patt.match(string)
# print(m)
# m = patt.match(string)
# print()
# print(m.groupdict())

# search:说明：在给定的字符串中寻找第一个匹配给正则表达式的子字符串，有多个也只返回第一个出现的。
# m = patt.search(string)
# print(m)
# print(m.group())

# findall: 说明：列表形式返回给定模式的匹配项。返回所有匹配的字符串。
# m = patt.findall(string)
# print(m)
# for m in m:
#     print(m)

patt1 = re.compile(r'(?P<first_name>[a-zA-Z]+)\s(?P<last_name>[a-zA-Z]+)')
# m=patt1.search(string).groupdict()
# print(m)

name = ("First name","Last name")
d = {}
m = patt1.findall(string)
# print(m)
for i in m:
    zipped = zip(name,i)
    d.update(dict(zipped))

print(d)

# Generator
m = patt1.finditer(string)
dict = {}
for i in m:
    print(type(i))
    dict.update(i.groupdict())

print(dict)
