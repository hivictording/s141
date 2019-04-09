# Author: Victor Ding

username = input("username:")
age = input("age:")
sex = input("sex:")
nationality = input("nationality:")

''''''
print(("""username is {a1}
age is {b1}
sex is {c1}
nationality is {d1}
""").format(a1=username, b1=age, c1=sex, d1=nationality))
''''''

print("""Your name is {0}
Your age is {1}
Your sex is {2}
Your nationality is {3}
""".format(username, age, sex, nationality)
      )

print(f"Your name is {username},age {age}, {sex}, nationality is {nationality}")

print(f"""Your name is {username},
age {age}, 
{sex}, 
nationality is {nationality}""")

print("""Your name is %s
your age is %s
your sex is %s
your nationality is %s
""" %(username,age,sex,nationality))

