# Author: Victor Ding

import yaml

# with open("house.yaml","r") as fh_house:
#     y = yaml.load(fh_house)
#
# print(y['house'])

users = {
        "Victor":{
                    "age":44,
                    "sex":"male",
                    "nationality":"China",
                    "Parents":{
                                "father":"Ding Yuyuan",
                                "mother":"Huang Huachu"
                    },
        },
        "Mary":{
                    "age":38,
                    "sex":"female",
                    "nationality":"China",
                    "Parents":{
                                "father":"Zhu Jinhua",
                                "mother":"Zhang Xiaolan"
                    },
        },
}

with open("users.yaml","w") as fh_users:
    yaml.dump(users,fh_users)