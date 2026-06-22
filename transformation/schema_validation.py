import pandas as pd

customers_df = pd.read_csv("../landing_zone/customers_raw.csv")

required_columns = [
    "customer_id",
    "customer_name",
    "city",
    "state"
]

if all(column in customers_df.columns for column in required_columns):
    print("Schema validation successful")
else:
    print("Schema validation failed")
