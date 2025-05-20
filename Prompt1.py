### Collection of Logic Programming Prompts
### Author: Viveka Cheekati
### Date: 11/19/2024

## Prompt 1.
## Write a Python program to analyze the performance of sales representatives. The program should:
sales_data = [
    {"rep_id": "R001", "name": "Alice", "month": "Jan", "sales": 15000},
    {"rep_id": "R001", "name": "Alice", "month": "Feb", "sales": 14000},
    {"rep_id": "R001", "name": "Alice", "month": "Mar", "sales": 12000},
    {"rep_id": "R002", "name": "Bob", "month": "Jan", "sales": 18000},
    {"rep_id": "R002", "name": "Bob", "month": "Feb", "sales": 20000},
    {"rep_id": "R002", "name": "Bob", "month": "Mar", "sales": 21000},
    {"rep_id": "R003", "name": "Charlie", "month": "Jan", "sales": 12000},
    {"rep_id": "R003", "name": "Charlie", "month": "Feb", "sales": 11000},
    {"rep_id": "R003", "name": "Charlie", "month": "Mar", "sales": 10000},
]
# Calculate the total sales for each representative.
def rep_total_sales(data):
    totals = dict()
    for i in data:
        keys = list(i.keys())
        reps = (i[keys[0]] + "_" + i[keys[1]])
        sales = keys[3]
        if(reps not in totals.keys()):
            totals[reps] = 0
        totals[reps] += i[sales]
    return totals
result = rep_total_sales(sales_data)
for i in result:
    print(f"{i}: ${result[i]}")
print()

# Determine the top performer(s) (sales above 90th percentile).
def top_perf(data, percentile):
    data = rep_total_sales(data)
    perf = [data[i] for i in data]
    perf.sort()
    threshold = (percentile/100) * (len(perf) + 1)
    top = []
    if(threshold is not int):
        threshold = int(round(threshold, 0))
    if(threshold > len(perf)):
        if(threshold - len(perf) <= 1):
            threshold = len(perf) - 1
        else:
            return top
    threshold = perf[threshold]
    for i in data:
        if(data[i] >= threshold):
            top.append(i)
    return top
top_performers = top_perf(sales_data, 90)
print(top_performers)
print()

# Identify representatives whose sales have decreased month-over-month for two consecutive months.
def mon_sales_lower(data):
    mon_sales = dict()
    decr_sales = []
    for i in data:
        keys = list(i.keys())
        reps = (i[keys[0]] + "_" + i[keys[1]])
        sales = keys[3]
        if(reps not in mon_sales.keys()):
            mon_sales[reps] = []
        mon_sales[reps].append(i[sales])
    for i in mon_sales:
        count = 0
        for j in range(len(mon_sales[i])):
            if(j == len(mon_sales) - 1):
                continue
            if(mon_sales[i][j] > mon_sales[i][j + 1]):
                count += 1
            if(count >= 2):
                decr_sales.append(i)
    return decr_sales
sales_decreasing_2month = mon_sales_lower(sales_data)
print(sales_decreasing_2month)
print()

# Provide a summary report.
def summary_report(data):
    summary = dict()
    for i in data:
        keys = list(i.keys())
        reps = (i[keys[0]] + "_" + i[keys[1]])
        mon = i[keys[2]]
        sales = i[keys[3]]
        if(mon not in summary.keys()):
            summary[mon] = dict()
        summary[mon][reps] = sales
    return summary
summary =  summary_report(sales_data)
for mon in summary.keys():
    print(f"{mon}")
    for emp in summary[mon]:
        print(f"{emp}: {summary[mon][emp]}\t", end = "\t")
    print('\n')
print()