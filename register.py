import re
import login


def reg():
    print("register")
    firstname = input("Please enter a firstname: ")
    lastname = input("Please enter a lastname: ")
    newemail = input("your email: ")
    while not re.match(r"^[a-zA-Z][a-zA-Z0-9\.]+\@[a-zA-Z]+\.[a-zA-Z]{3}", newemail):
        newemail = input("your email: ")
    password = input("Now password: ")
    repassword = input("Now Retype password: ")
    while password != repassword:
        repassword = input("Now Retype password: ")
    file = open("login.txt", "a")
    file.write(firstname)
    file.write(",")
    file.write(lastname)
    file.write(",")
    file.write(newemail)
    file.write(",")
    file.write(password)
    file.write("\n")
    file.close()
    print("Your login details have been saved. ")
    print("You need to login now")
    login.log()
