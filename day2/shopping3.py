# Author: Victor Ding

import json

shopping_list = []

print("Welcome to Walmart Superstore!".center(200,"*"))

try:
    with open("products.json","r") as fh_products:
        items_json = fh_products.read()
        items = json.loads(items_json)
except FileNotFoundError:
    exit("Sorry, no goods left in Walmart right now, please visit at a later time......")

while True:
    balance = input("Please input your account balance:")
    if balance.isdigit():
        balance = int(balance)

        while True:
        # introduce the price list
            print("Here are the product list:".center(200,'*'))
            print("Product Code       Product Name -------------------->                 Price")
            for item in items:
                print("{0}                   {1}  -------------------->                        {2}".format(item,items[item]['name'],items[item]['price']))
            option = input("Please select a product code to shop, or you can input 'q' to exit anytime:")
            if option.isdigit():
                int_option = int(option)
                if int_option >=0 and int_option < len(items):
                    item_price = items[int_option][1]
                    if balance >= item_price:
                        balance -= item_price
                        shopping_list.append(items[int_option])
                        print("congratulations, you've successfully purchased %s, your current balance is %s" % (items[int_option][0],balance))
                    else:
                        print("Sorry, purchase failed, only %s left on your account" % balance)
                else:
                    print("%s is not a valid product code, Please input a valid code to continue" % option)
            elif option == 'q':
                print("Thanks for visiting Walmart Online Shop")
                print("Below are what you've purchased today, your current balance is %s" % balance)
                for item in shopping_list:
                    print(item)
                print("\n\n\nSee you next time!")
                exit()
            else:
                print("Wrong code received!")
    else:
        print("You have entered an invalid balance number, please enter again")
