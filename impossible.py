import random
guess = 5
randomnumber= random.randint
randomnumber = int(input("enter a number between -1000000000000000 and 1000000000000000 "))
number = 876987
chances = 1
while chances > 0:
    if randomnumber == number:                                                                                                                            
        print("OH NO!! MY WINSTREAK!! IT'S BROKEN!! (ノಠ益ಠ)ノ彡┻━┻")
        print("(The number was", number, ")")
        break
    elif randomnumber == number:                                                                                                        
        print("That's not right, you  f o o l i s h   i d i o t ! ")
        chances - 1
        break
    elif chances == 0:
        print("You lose and you are a failure! no wonder you are lonely! go eat a glass sandwich!")
        break