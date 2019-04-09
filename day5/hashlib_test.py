# Author: Victor Ding

import hashlib,hmac

m = hashlib.sha512()
m.update(b"victor")
print(m.hexdigest())

m2 = hashlib.sha512()
m2.update("victor".encode(encoding='utf-8'))
print(m.hexdigest())

m3 = hmac.new(b"123",b"victormary")
print(m3.hexdigest())

m4 = hmac.new(b"123",b"victor")
m4.update("mary".encode(encoding='utf-8'))
print(m4.hexdigest())