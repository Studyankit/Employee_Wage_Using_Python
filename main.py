import random

print("Welcome to Employee Wage Computation")

wage_per_hour = 20
full_day_hour = 8
working_days = 20
part_time_hour = 5
working_day_per_month = 20
emp_hrs = 0


# UC1 - Employee Attendance


def Attendance(present=0, absent=0):
    for i in range(20):
        attendance_check = random.randint(0, 2)
        if attendance_check == 1:
            present += 1
        else:
            absent += 1
        return present


# UC2  - Daily Wage

def Daily_Wage():
    daily_wage = wage_per_hour * full_day_hour
    return daily_wage


# Uc3 - Part time and full time

def Part_Time_Wage():
    part_time = part_time_hour * wage_per_hour
    return part_time


def Daily_Wage_Ft_Pt():
    emp_check = random.randint(0, 2)
    if emp_check == 1:
        part_time = part_time_hour * wage_per_hour
        return part_time
    elif emp_check == 2:
        daily_wage = wage_per_hour * full_day_hour
        return daily_wage
    else:
        return 0


# Uc4 - Wage for month


def Monthly_Wage():
    month_wage = 0
    for day in range(1, 21):
        emp_data = {"Day": day, "Wage": Daily_Wage_Ft_Pt()}
        print(emp_data)
        sum_wage = emp_data["Wage"]
        month_wage += sum_wage
    print(month_wage)


Monthly_Wage()
