import random

def calculate_daily_wage(wage_per_hour):
    attendance = random.randint(0, 2)

    match attendance:
        case 1:
            daily_wage = wage_per_hour * 8
            print(f"Employee is Present (Full-time). Daily Wage: {daily_wage}")
        case 2:
            daily_wage = wage_per_hour * 4
            print(f"Employee is Present (Part-time). Daily Wage: {daily_wage}")
        case _:
            print("Employee is Absent. Daily Wage: 0")

calculate_daily_wage(20)