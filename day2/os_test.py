# Author: Victor Ding
import os

# pointer = os.popen("dir")
# result = pointer.read()

pointer = os.popen("dir test")
result = pointer.read()

print(result)