# Author: Victor Ding

import copy

names = ['vmware','sonicwall','red hat','cisco',['F5', 'Watchguard'],'juniper','palo alto','arista']

names_2 = copy.deepcopy(names)
names_3 = copy.copy(names)
names_4 = names.copy()
names_5 = names[:]
names_6 = list(names)

names[4][1] = 'Sophos'
names[0] = 'Extreme'

print(names)
print(names_2)
print(names_3)
print(names_4)
print(names_5)
print(names_6)