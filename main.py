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

# UC2  - Daily Wage

wage_per_hour = 20
full_day_hour = 8


def Daily_Wage():
    daily_wage = wage_per_hour * full_day_hour
    print(f"Full day wage of an employee {daily_wage}")


print(Daily_Wage())
