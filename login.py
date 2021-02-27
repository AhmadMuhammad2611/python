import project


def log():
    print("login")
    username1 = input("Please enter your email: ")
    password1 = input("Please enter your password: ")

    file = open("login.txt", "r")
    for row in file:
        field = row.split(",")
        newemail = field[2]
        password = field[3]
        lastchar = len(password)-1
        password = password[0:lastchar]

        if username1 == newemail and password1 == password:
            print("Hello", newemail)
            project.proj()
            break
    else:
        print("incorrect")
        log()


# file.close()
# log()
#####################
# lastchar = len(password)-1
# password = password[0:lastchar]
# for row in file:
#     field = row.split(",")
#     username = field[0]
#     password = field[1]
#     lastchar = len(password)-1
#     password = password[0:lastchar]

#     if username1 == username and password1 == password:
#         print("Hello",username)
#         break
# else:
#     print("incorrect")
