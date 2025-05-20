### Collection of Logic Programming Prompts
### Author: Viveka Cheekati
### Date: 11/20/2024

## Prompt 4.
## Create a program to dynamically adjust product prices based on demand. The program should:
product_data = [
    {"product_id": "P001", "name": "Widget", "price": 100, "demand": [100, 120, 140]},
    {"product_id": "P002", "name": "Gadget", "price": 200, "demand": [80, 75, 70]},
    {"product_id": "P003", "name": "Doodad", "price": 150, "demand": [200, 190, 195]},
    {"product_id": "P004", "name": "Thingamajig", "price": 50, "demand": [50, 55, 60]},
]

# Increase prices by 10% if demand has increased by more than 15% month-over-month.
# Decrease prices by 5% if demand drops by more than 10%.
# Keep prices unchanged if demand changes are within 10%.
def chng_prices(data):
    for row in data:
        keys = list(row.keys())
        price = row[keys[2]]
        demand = row[keys[3]]
        change = 0
        for i in range(int(len(demand)) - 1):
            change += ((demand[i+1] - demand[i])/demand[i])
        if(change >= 0.15):
            row[keys[2]] = round(1.10 * price, 2)
        elif(change <= -0.1):
            row[keys[2]] = round(0.95 * price, 2)
        elif(abs(change) < 0.1):
            continue
    return data
res = chng_prices(product_data)
for i in res:
    print()
    for j in i.keys():
        print(j, i[j])
print("----------------------")
print()

# Generate a pricing report for all products.
def gen_report(data):
    report = []
    for row in data:
        keys = list(row.keys())
        id = row[keys[0]] + "_" + row[keys[1]]
        price = round(row[keys[2]], 2)
        report.append({id:price})
    return report
res = gen_report(product_data)
for row in res:
    for keys in row.keys():
        print(f"{keys}: ${row[keys]}")
print()