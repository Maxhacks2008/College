import random
number = random.randint(1,2)
print (number)
if number == 1:
    ask = input("What is your favorite person")
    if ask == "Maxime":
        print("Ahh you are so generouse")
    else:
        print("okay not that of a bad person")
elif number == 2:
    ask2 = input("What is your name")
    if ask2 < 18:
        print ("Ohh so you are still a minor")
    elif ask2 >= 18:
        print("ohh so you are an adult")
    else:
        print("Sorry that is a wrong input")
