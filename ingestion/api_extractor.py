import json

with open("../sample_data/api_response.json", "r") as file:
    api_data = json.load(file)

print("API Product Data:")

for product in api_data["products"]:
    print(product)
