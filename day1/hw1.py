# Author: Victor Ding

import json

users = {"victor":{"password":"111","status":"enabled"},"mary":{"password":"222","status":"enabled"},"mario":{"password":"333","status":"enabled"}}

# with open("users.json","w") as f:
# #     json = json.dumps(users)
# #     f.write(json)
# #     f.close()

with open("users.json","w") as fh_users:
    json.dump(users,fh_users)