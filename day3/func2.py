# Author: Victor Ding

def test(**kwargs):
    kwargs["test"] = "20190305"

    for v in kwargs.values():
        print(v)

    for i in kwargs.items():
        print(i)

test(name ="victor", sex ="male", age =44)