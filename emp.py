import random
def calculate_wages_until_condition(wage_per_hour):
    total_wage = 0
    working_days = 20
    total_hours = 0
    working_days = 0
    while total_hours < 100 and working_days < 20:
        attendance = random.randint(0, 2)

        match attendance:
            case 1:
                total_wage += wage_per_hour * 8
                total_hours += 8
                working_days += 1
            case 2:
                total_wage += wage_per_hour * 4
                total_hours += 4
                working_days += 1
            case _:
                pass

    print(f"Total Monthly Wage: {total_wage}")
    print(f"Total Wage: {total_wage}")
    print(f"Total Hours Worked: {total_hours}")
    print(f"Total Days Worked: {working_days}")
calculate_wages_until_condition(20)