import pandas as pd

# Source data
source_df = pd.read_csv("../landing_zone/customers_raw.csv")

# Target data
target_df = pd.read_csv("../staging/customers_stage.csv")

source_count = len(source_df)
target_count = len(target_df)

if source_count == target_count:
    status = "PASS"
else:
    status = "FAIL"

print("Source Count :", source_count)
print("Target Count :", target_count)
print("Status :", status)
