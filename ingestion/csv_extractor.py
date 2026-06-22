import pandas as pd

# Read customers data
customers_df = pd.read_csv("../sample_data/customers.csv")

# Read products data
products_df = pd.read_csv("../sample_data/products.csv")

print("Customers Data:")
print(customers_df.head())

print("\nProducts Data:")
print(products_df.head())
