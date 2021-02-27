import datetime


def proj():
    print("Welcome To projects")
    yourchoice = input("""choose 1,2 or 3
    1) create project
    2) list project
    3) delete project
    """)

    if yourchoice == "1":
        title = input("Please enter a title: ")
        details = input("Please enter a details: ")
        total = input("your total: ")
        dayDate = int(input("enter day number: "))
        monDate = int(input("enter month number: "))
        while datetime.datetime(year=2021, month=monDate, day=dayDate) <= datetime.datetime.now():
            dayDate = int(input("enter day number: "))
            monDate = int(input("enter month number: "))
        endDay = int(input("enter end day number: "))
        endMon = int(input("enter end month number: "))
        while datetime.datetime(year=2021, month=endMon, day=endDay) <= datetime.datetime.now() or datetime.datetime(year=2021, month=endMon, day=endDay) <= datetime.datetime(year=2021, month=monDate, day=dayDate):
            endDay = int(input("enter end day number: "))
            endMon = int(input("enter end month number: "))
        global file
        file = open("project.txt", "a")
        file.write(title)
        file.write(",")
        file.write(details)
        file.write(",")
        file.write(total)
        file.write(",")
        file.write(str(dayDate)+"-"+str(monDate))
        file.write(",")
        file.write(str(endDay)+"-"+str(endMon))
        file.write("\n")
        file.close()
        proj()
    # elif yourchoice == "2":
    #     for row in file:
    #         field = row.split(",")
    #     print(field)
