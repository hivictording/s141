def deco(func):
    def wrapper(*args,**kwargs):
        f = func()
        next(f)
        return f
    return wrapper

@deco
def fruits():
    fruits_list = []
    while True:
        fruit = yield fruits_list
        fruits_list.append(fruit)
        print('Here is the latest fruits we have:')


# fruits = deco(fruits)

f = fruits()
# print(next(f))
print(f.send('Pear'))
print(f.send('Apple'))
print(f.send('BlueBerry'))


