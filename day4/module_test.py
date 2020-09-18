# Author: Victor Ding

import os, sys

# current_path = os.path.abspath(__file__)
# current_dir = os.path.dirname(current_path)
# module_dir = current_dir+'\\modules'

current_dir = os.getcwd()
module_dir = current_dir+'\\modules'

# print(current_path)
print(current_dir)
print(module_dir)

sys.path.insert(1,module_dir)

import module1 as mod
from module1 import sub as s
from module1 import mul as m

mod.add(2,8)
s(8,2)
m(3,5)

