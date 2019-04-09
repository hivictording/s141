# Author: Victor Ding

import pickle

with open("users.pickle","rb") as fh_users:
    dict_users = pickle.load(fh_users)

for i in range(3):
    name = input("Please enter your username:")
    pswd = input("Please enter your password:")

    if name in dict_users:
        if dict_users[name]["status"] == "enabled":
            if dict_users[name]["password"] == pswd:
                print("Congratulations! User %s has been logged in the system!" %(name))
                break
            else:
                print("You have entered wrong username or password!")
        else:
            print("Your account has been locked, please ask for admin for assistance.")
            break
    else:
        print("You have entered wrong username or password!")

    if i == 2:
        dict_users[name]["status"] = "disabled"
        # json_users = json.dumps(dict_users)
        with open("users.pickle","wb") as fh_users:
            pickle.dump(dict_users,fh_users)
            fh_users.close()