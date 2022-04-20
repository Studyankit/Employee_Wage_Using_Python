import random

print("Welcome to Employee Wage Computation")


# UC1 - Employee Attendance
def Attendance():
    attendance_check = random.randint(0, 2)
    if attendance_check == 1:
        print("Employee is present")
    else:
        print("Employee is absent")


print(Attendance())
