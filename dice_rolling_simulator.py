# importing the module for rolling dice
import random

#Appling the loop for contineous result
while True:
    # Applying the input using the randint function and store it in variable
    a = random.randint(1,6)
    b = random.randint(1,6)

    # To ptint the result and their sum
    print(a)
    print(b)
    print("The sum of two numbers",(a+b))

    # If the same numbers on the same rolling then one more chance give to them
    if a == b:
        print("Doubles!! One more chance!!")
    # for next itteration use the input statement.
    input("Press the enter key to go to next result")



