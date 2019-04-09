# Author: Victor Ding

import json

menu = ["Add a item","Modify a item","Quit",]

try:
    with open("products.json","r") as fh:
        f_json = fh.read()
        f_dict = json.loads(f_json)
        fh.close()
except FileNotFoundError:
    f_dict = {}

while True:
    print("\n\n\n")
    print("Welcome to the warehouse system,!".center(200,"+"))
    for i, m in enumerate(menu):
        print(i, "    ------->     ", m)
    option = input("Please select a number to operate:")
    if option.isdigit():
        option = int(option)
        if option == 0:  # Adding an item
            item_number = input("Please input the item number you want to add:(between 1 to 9999)")
            item_name = input("Please input the item name you want to add:")
            item_price = input("Please input the item price you want to add:")
            if item_number.isdigit() and int(item_number) >=1 and int(item_number) < 10000:
                if item_price.replace(".","",1).isdigit():
                    item_price = float(item_price)
                    if item_number not in f_dict:
                        f_dict[item_number] = {"name":item_name,"price":item_price}
                        print("You have successfully added {number}:{name} to the database!".\
                              format(number =item_number,name =item_name))
                    else:
                        print("The item {number}:{name} is already in the database.....".format(number =item_number,name =item_name))
                else:
                    print("You have entered an invalid 'item price")
            else:
                print("You have entered an invalid 'item number'!")
        elif option == 1:  # Modifying an item
            item_number = input("Please input the item number you want to modiy:")
            if item_number.isdigit() and int(item_number) >=1 and int(item_number) < 10000:
                if item_number in f_dict:
                    item_name = f_dict[item_number]["name"]
                    item_price = input("Please input the new price of %s %s:" % (item_number,item_name))
                    if item_price.replace(".","",1).isdigit():
                        item_price = float(item_price)
                        f_dict[item_number]["price"] = item_price
                        print("You have successfully modified the price of {number}:{name} in the database!".format(number =item_number,name =item_name))
                    else:
                        print("You have entered an invalid 'item price")
                else:
                    print("The item number %s is not in the database!" % item_number)
            else:
                print("You have entered an invalid 'item number'!")
        elif option == 2:  # Quitting
            f_json = json.dumps(f_dict)
            with open("products.json","w") as fh_products:
                fh_products.write(f_json)
            exit()
        else:
            print("You have entered an invalid option!")
    else:
        print("You have entered an invalid option!")
