# Author: Victor Ding
import json

print("Welcome aboard!")

# with open("users.json","r") as f_users:
#     json_users = f_users.read()
#     dict_users = json.loads(json_users)
#     f_users.close()

with open("users.json", "r") as fh_users:
    dict_users = json.load(fh_users)

with open("userinfo.txt", "r") as f_userinfo:
    locked_user = f_userinfo.readlines()
    f_userinfo.close()

# print(dict_users)

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
        json_users = json.dumps(dict_users)
        with open("users.json","w") as f_users:
            f_users.write(json_users)
            f_users.close()
        locked_user.append(name)
        with open("userinfo.txt","w") as f_userinfo:
            f_userinfo.writelines("{}\n".format(user) for user in locked_user)

