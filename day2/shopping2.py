# Author: Victor Ding

items = [
    ("Apple",5),
    ("Orange",3),
    ("Grape", 7),
    ("Blueberry",10),
    ("Rasberry", 6),
    ("Pear",4),
    ("Watermelon",8),
    ("Dates",15),
    ("Lemon",3),
    ("Avacado",16),
    ("Brocolli",4),
    ("Spinach",5),
    ("Turnip",8),
    ("Cauliflower",5),
    ("Pork Belly",7),
    ("Beef Belly",13),
    ("Flounder Fish", 25),
]

shopping_list = []

print("Welcome to Walmart Superstore!".center(200,"*"))

while True:
    balance = input("Please input your account balance:")
    if balance.isdigit():
        balance = int(balance)

        while True:
        # introduce the price list
            print("Here are the product list:".center(200,'*'))
            print("Product Code        -------------------->            Price")
            for index,item in enumerate(items):
                print("{0}                   -------------------->                 {1}".format(index,item))
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
