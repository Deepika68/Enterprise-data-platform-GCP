import pandas as pd
from datetime import datetime

audit_data = {
    "run_date": [datetime.now()],
    "source_count": [5],
    "target_count": [5],
    "status": ["PASS"]
}

audit_df = pd.DataFrame(audit_data)

audit_df.to_csv(
    "audit_table.csv",
    index=False
)

print("Audit log generated successfully")
