# Author: Victor Ding

import shelve

# users_db["victor"] = {"age":44,"sex":"male","city":"markham","job":"IT"}
# users_db["mary"] = {"age": 38, "sex": "female", "city": "markham", "job": "unemployed"}
# users_db["mario"] = {"age": 6, "sex": "male", "city": "markham", "job": "child"}

def add(db):
    name = input("name:")
    age = input("age:")
    sex = input("sex:")
    city = input("city:")
    job = input("job:")
    db[name] = {"age":int(age),"sex":sex,"city":city,"job":job}
    print(f"You have successfully added user {name}.....")

def delete(db):
    name = input("please input the name you want to delete:")
    del db[name]
    print(f"You have successfully deleted user {name}.....")

def search(db):
    name = input("please input the name you want to search:")
    print(f"Below is the user information for {name}")
    print("Age:{age}, Sex:{sex}, City:{city},Job:{job}".format(age=db.get(name).get("age"),sex=db[name]["sex"],\
          city=db[name]["city"],job=db.get(name)["job"]))

def update(db):
    name = input("Please input the name you want to modify:")
    item = input("Which item do you want to modify? age,sex,city,job?")
    new_data = input("Please input the new data of %s:" % item)
    db[name][item] = new_data
    print(f"You have successfully updated user {name} {item} to {new_data}.....")

def main():
    users_db = shelve.open("users.db", writeback=True)

    try:
        while True:
            cmd = input("Please input the operation command:")
            if cmd == "add":
                add(users_db)
            elif cmd == "search":
                search(users_db)
            elif cmd == "update":
                update(users_db)
            elif cmd == "delete":
                delete(users_db)
            elif cmd == "quit":
                return
            else:
                print("you have input an invalid command.....")
    finally:
        users_db.close()

if __name__ == "__main__":
    main()

