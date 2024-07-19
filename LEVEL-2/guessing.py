import random
Cnumber = random.randrange(1,101)

user_input = int(input("Enter your number:--"))

if user_input>Cnumber:
    print("Computer Number", Cnumber)
    print("your guess Number is high")
elif Cnumber >  user_input:
    print("Computer Number", Cnumber)
    print("your guess number is low")
else:
    print("Computer Number", Cnumber)
    print("your guess number is equal")
