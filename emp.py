import random
class Employee:
    wage_per_hour = 20
    total_wage = 0
    total_hours = 0
    working_days = 0
    @classmethod
    def calculate_wages_until_condition(cls, max_hours=100, max_days=20):
        while cls.total_hours < max_hours and cls.working_days < max_days:
            attendance = random.randint(0, 2)
            match attendance:
                case 1:
                    cls.total_wage += cls.wage_per_hour * 8
                    cls.total_hours += 8
                    cls.working_days += 1
                case 2:
                    cls.total_wage += cls.wage_per_hour * 4
                    cls.total_hours += 4
                    cls.working_days += 1
                case _:
                    pass
        print(f"Total Wage: {cls.total_wage}")
        print(f"Total Hours Worked: {cls.total_hours}")
        print(f"Total Days Worked: {cls.working_days}")

employee = Employee()
employee.calculate_wages_until_condition()