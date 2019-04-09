# Author: Victor Ding

age = 35
#i = 0

#count = 0

for count in range(0,3):
    guess_age = int(input("what is the age you guess this time?"))
    if guess_age == age:
        print("Bingo!")
        break
    elif guess_age < age:
        print("too young!")
    else:
        print("too old!")
else:
    print("Game Over!")


