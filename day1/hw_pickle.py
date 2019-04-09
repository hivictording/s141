# Author: Victor Ding

import pickle

users = {"victor":{"password":"111","status":"enabled"},"mary":{"password":"222","status":"enabled"},"mario":{"password":"333","status":"enabled"}}

with open("users.pickle","wb") as fh_users:
    pckl = pickle.dump(users,fh_users)