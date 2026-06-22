import json

with open("../sample_data/orders.json", "r") as file:
    orders_data = json.load(file)

print("Orders Data:")

for order in orders_data:
    print(order)
