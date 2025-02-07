import random
def check_attendance():
    print("Welcome to Employee wage program on Master Branch")
    attendance = random.randint(0, 1)
    if attendance == 1:
        print("Employee is Present")
    else:
        print("Employee is Absent")
check_attendance()
