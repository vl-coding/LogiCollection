### Collection of Logic Programming Prompts
### Author: Viveka Cheekati
### Date: 11/20/2024

## Prompt 3.
## Write a program to calculate performance-based bonuses for employees. Bonuses are calculated as follows:
employee_data = [
    {"emp_id": "E001", "name": "John", "base_salary": 50000, "target": 100000, "actual_sales": 120000},
    {"emp_id": "E002", "name": "Jane", "base_salary": 60000, "target": 150000, "actual_sales": 140000},
    {"emp_id": "E003", "name": "Jim", "base_salary": 55000, "target": 130000, "actual_sales": 100000},
    {"emp_id": "E004", "name": "Jill", "base_salary": 70000, "target": 200000, "actual_sales": 250000},
]
# Employees exceeding their target by 20% or more receive a 15% bonus on their base salary.
def exceed_target(data):
    exceeded = dict()
    for emp in data:
        keys = list(emp.keys())
        id = emp[keys[0]] + "_" + emp[keys[1]]
        base = emp[keys[2]]
        target = emp[keys[3]]
        actual = emp[keys[4]]
        if(actual >= (1.2 * target)):
            exceeded[id] = 0.15*base
    return exceeded
res = exceed_target(employee_data)
for i in res.keys():
    print(f"{i}: ${res[i]}")
print()

# Employees meeting their target receive a 10% bonus.
def meet_target(data):
    meet = dict()
    for emp in data:
        keys = list(emp.keys())
        id = emp[keys[0]] + "_" + emp[keys[1]]
        base = emp[keys[2]]
        target = emp[keys[3]]
        actual = emp[keys[4]]
        if(target == actual or (actual < 1.2 * target and actual > target)):
            meet[id] = 0.1*base
    return meet
res = meet_target(employee_data)
for i in res.keys():
    print(f"{i}: ${res[i]}")
print()

# Employees below their target but above 80% of the target receive a 5% bonus.
def below_target(data):
    below = dict()
    for emp in data:
        keys = list(emp.keys())
        id = emp[keys[0]] + "_" + emp[keys[1]]
        base = emp[keys[2]]
        target = emp[keys[3]]
        actual = emp[keys[4]]
        if(actual < target and actual > (0.8 * target)):
            below[id] = 0.05*base
    return below
res = below_target(employee_data)
for i in res.keys():
    print(f"{i}: ${res[i]}")
print()

# Generate a report showing each employee's bonus and their performance category.
def gen_report(data):
    report = [{"Exceeded target":dict()}, {"Meet target":dict()}, {"Below target":dict()}]
    exceed = exceed_target(data)
    meet = meet_target(data)
    below = below_target(data)
    for emp in data:
        keys = list(emp.keys())
        id = emp[keys[0]] + "_" + emp[keys[1]]
        if(id in list(exceed.keys())):
            report[0][list(report[0].keys())[0]] = {id:exceed[id]}
        elif(id in list(meet.keys())):
            report[1][list(report[1].keys())[0]] = {id:meet[id]}
        if(id in list(below.keys())):
            report[2][list(report[2].keys())[0]] = {id:below[id]}
    return report
res = gen_report(employee_data)
for i in res:
    for j in i:
        print(f"{j}")
        for info in i[j]:
            print(f"{info}: ${i[j][info]}")
        print()