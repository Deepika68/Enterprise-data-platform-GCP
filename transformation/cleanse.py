import pandas as pd

customers_df = pd.read_csv("../landing_zone/customers_raw.csv")

# Remove duplicates
customers_df = customers_df.drop_duplicates()

# Fill missing values
customers_df = customers_df.fillna("Unknown")

# Save stage file
customers_df.to_csv(
    "../staging/customers_stage.csv",
    index=False
)

print("Data cleansing completed")
