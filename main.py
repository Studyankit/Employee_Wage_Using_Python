import random

print("Welcome to Employee Wage Computation")

wage_per_hour = 20
full_day_hour = 8
part_time_hour = 6
WORKING_DAY_PER_MONTH = 20
TOTAL_WORKING_HRS = 100


# UC1 - Employee Attendance


def Attendance(present=0, absent=0):
    """

    :param present: Employee present for how many days
    :param absent: Employee absent for how many days
    :return: No days present
    """

    for i in range(20):
        attendance_check = random.randint(0, 2)
        if attendance_check == 1:
            present += 1
        else:
            absent += 1
        return present


# UC2  - Daily Wage

def Daily_Wage():

    """
    Calculate daily wage for an employee

    :return: return daily wage
    """
    daily_wage = wage_per_hour * full_day_hour
    return daily_wage


# Uc3 - Part time and full time

def Part_Time_Wage():

    """
    Calculate Part-time wage of an employee with work hr 6

    :return: part- time wage of emp
    """
    part_time = part_time_hour * wage_per_hour
    return part_time


def Daily_Wage_Ft_Pt():
    """
    Calculate Daily Wage according to no of hr worked

    :return: Wage according to parT time hr or full time hr
    """
    emp_check = random.randint(0, 2)
    if emp_check == 1:
        part_time = part_time_hour * wage_per_hour
        return part_time, part_time_hour
    elif emp_check == 2:
        daily_wage = wage_per_hour * full_day_hour
        return daily_wage, full_day_hour
    else:
        return 0, 0


# Uc4,5,6.. - Wage for month  with total working hrs


def Monthly_Wage():
    """
    Calculate monthly wage with storing the data in dictionary with his regular days work and attendance

    :return: monthly wage with the total hrs worked
    """
    month_wage = 0
    total_hrs = 0
    for day in range(1, 21):
        emp_data = {"Day": day, "Wage": Daily_Wage_Ft_Pt()}
        print(emp_data)
        sum_wage = emp_data["Wage"][0]
        month_wage += sum_wage
        total_hrs += emp_data["Wage"][1]
        if total_hrs >= 100:
            break
    print(month_wage)
    print(total_hrs) # Uc6 - total hr worked


Monthly_Wage()

