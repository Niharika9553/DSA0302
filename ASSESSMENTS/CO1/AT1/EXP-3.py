import re

name = input("Enter Name: ")
email = input("Enter Email: ")

# Validate Name and Email
if re.fullmatch("[A-Za-z ]+", name) and re.fullmatch(r"\w+@\w+\.\w+", email):
    print("Registration Successful")
else:
    print("Registration Failed")
