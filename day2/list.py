# Author: Victor Ding

names = ['vmware','sonicwall','red hat','cisco','juniper','palo alto','arista']

names.append('fortinet') # insert at the end

names[2] = 'citrix' # replace specific element

names.insert(2,'extreme')

# How to delete elments
names.remove('arista')
print(names)
names.__delitem__(names.index('juniper'))
del names[names.index('cisco')]
print(names)
names.pop()
names.pop(2)

names.append('sonicwall')



print(names)
print(names[-2:])   # slice

print(names.count('sonicwall'))

names.extend(i for i in range(5))

print(names)

del names

print(names)