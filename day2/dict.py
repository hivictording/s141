# Author: Victor Ding

dict_users = dict.fromkeys(['a','b','c'],list(i for i in range(3)))

print(dict_users)

for d in dict_users:
    print(d)
    print(dict_users.get(d))

for k,v in dict_users.items():
    print(k,v)