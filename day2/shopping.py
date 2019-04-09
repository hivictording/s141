# Author: Victor Ding

items = [[1,"Pork belly",20],[2,"Beef belly",40],[3,"Large eggs",4],[4,"Flounder fish",50],[5,"Milk",3],[6,"Bean Sprout",6],[7,"Banana",2],[8,"Roasted Chicken",9],[9,"Apple",4],[10,"Chicken leg",8]]

# Generate a list for item numbers
item_numbers = list(i[0] for i in items)

shopped_items = []

print("Welcome to Walmart!")
balance = int(input("Please input your current account balance:     "))

while True:
    print("Please see below for the shopping items:")
    for item in items:
        print(item)
    option = input("select the number on the left to shop, input 'q' anytime to quit:")
    if option == 'q':
        print("You have purchased:")
        for i in shopped_items:
            print("{0}   ------     {1}".format(i[0],i[1]))
        exit("Thanks for shopping, see you next time!")
    else:
        int_option = int(option) - 1
        cost = items[int_option][2]
        if cost <= balance:
            shopped_items.append([items[int_option][1],items[int_option][2]])
            print("Congratulations! '{0}' has been added to your cart.".format(items[int_option][1]))
            balance = balance - cost
        else:
            print("Sorry, you don't have enough balance!")




