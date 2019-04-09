# Author: Victor Ding

def h(alist):
    for a in alist:
        m = yield a+10
        print("first yield:",m)
        n = yield a+20
        print("second yield:",n)

# for i in h():
#     print(i)
blist = h([1,2,3,4,5])

res = blist.send(None)  # 等于 "h.next()"
print(res)

res = blist.send(100)
res = blist.__next__()
print(res)

res = blist.send(101)
print(res)
