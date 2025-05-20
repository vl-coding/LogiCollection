### Collection of Logic Programming Prompts
### Author: Viveka Cheekati
### Date: 11/20/2024

## Prompt 2.
## Design a program to analyze inventory data and suggest items for restocking. The program should:
inventory_data = [
    {"item_id": "I001", "name": "Laptop", "stock": 15, "reorder_level": 20, "monthly_sales": [10, 15, 18]},
    {"item_id": "I002", "name": "Keyboard", "stock": 50, "reorder_level": 30, "monthly_sales": [5, 8, 7]},
    {"item_id": "I003", "name": "Mouse", "stock": 5, "reorder_level": 10, "monthly_sales": [20, 25, 22]},
    {"item_id": "I004", "name": "Monitor", "stock": 2, "reorder_level": 5, "monthly_sales": [3, 2, 1]},
]

# Identify items below their reorder level.
def below_reorder(data):
    below = []
    for items in data:
        keys = list(items.keys())
        name = items[keys[0]] + "_" + items[keys[1]]
        stock = items[keys[2]]
        reorder = items[keys[3]]
        if(stock < reorder):
            below.append({name:(reorder - stock)})
    return below
res = below_reorder(inventory_data)
for i in res:
    for j in i.keys():
        print(f"{j}: {i[j]}")
print()

# Suggest restocking quantity based on average monthly sales over the last 3 months.
def restock(data, last_mons):
    restock_items = []
    for items in data:
        keys = list(items.keys())
        name = items[keys[0]] + "_" + items[keys[1]]
        stock = items[keys[2]]
        reorder = items[keys[3]]
        mon_sales = items[keys[4]]
        sum = 0
        for mon in range(last_mons):
            sum += mon_sales[len(mon_sales) - 1 - last_mons]
        avg = sum/len(mon_sales)
        restock = avg * len(mon_sales) - stock
        if(restock > 0):
            restock_items.append({name:int(restock)})
    return restock_items
res = restock(inventory_data, 3)
for i in res:
    for j in i.keys():
        print(f"{j}: {i[j]}")
print()

# Flag items that are moving slowly (average monthly sales < 10 units).
def flag_items(data):
    flagged = []
    for items in data:
        keys = list(items.keys())
        name = items[keys[0]] + "_" + items[keys[1]]
        mon_sales = items[keys[4]]
        sum = 0
        for mon in mon_sales:
            sum += mon
        avg = sum/len(mon_sales)
        if(avg < 10):
            flagged.append(name)
    return flagged
res = flag_items(inventory_data)
for i in res:
    print(i)
print()