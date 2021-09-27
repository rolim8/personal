import random
import time

print("\n//-----------Welcome to LuckyD20-----------//")

v_min = 1
v_max = 20

roll_again = "y"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices..."), time.sleep(2)
    print("The values are...")   , time.sleep(1)
    print(random.randint(v_min, v_max))

    print("\n//-----------------------------------------//")
    roll_again = input("Roll the dice again?(y/n) ")

if roll_again == "n":
    print("\n*********************"
          "\n** ATÉ A PRÓXIMA! **"
          "\n*********************\n")