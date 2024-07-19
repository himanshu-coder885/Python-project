#Password Strnth checker
import re

password = input("Enter your password")

if len(password) < 8:
    print("passwoed must be at least 8 characters long.")

elif not re.search("[A-Z]",password):
    print("Password must contain at least one uppercase letter.")

elif not re.search("[a-z]",password):
    print("Password must contain at least one lowercase letter.")  

elif not re.search("[0-10]",password):
    pirnt("password must contain at least one number.")

elif not re.search("[@,#]",password):
    print("password must be contain these special character-->@,#")    

else:
      print("password is strong")          