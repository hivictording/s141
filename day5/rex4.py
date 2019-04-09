# Author: Victor Ding

import re

def update_tel(a,b):
    patt = re.compile(r'\(?(?P<country_code>\w{3})\)?-?(?P<area_code>\w{3})-(?P<number>\w{4,10})')
    with open(a,'r',encoding='utf-8') as fh_a,open(b,'w') as fh_b:
        for line in fh_a:
            m = patt.sub(_replace,line)
            # m = patt.sub('\g<country_code>\g<area_code>\g<number>',line)
            fh_b.write(m)

def _replace(m):
    country_code = m.group("country_code")
    area_code = m.group("area_code")
    number = m.group("number")
    return '('+country_code+')'+'['+area_code+']'+'-'+number

if __name__ == "__main__":
    update_tel("tel2.ini","new_tel.ini")

"""
sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]): 
使用repl替换string中每一个匹配的子串后返回替换后的字符串。 
当repl是一个字符串时，可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。 
当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。 
count用于指定最多替换次数，不指定时全部替换。 

import re
 
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
 
print p.sub(r'\2 \1', s)
 
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
 
print p.sub(func, s)
 
### output ###
# say i, world hello!
# I Say, Hello World!

"""