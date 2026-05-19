import pandas as pd
import numpy as np

# Run this to generate the messy data
raw_data = {
    'Emp_ID': [101, 102, 102, 104, 105, np.nan],
    'Name': [' Alice ', 'Bob', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', ' hr', 'HR', 'IT', 'sales', 'Marketing'],
    'Salary': ['$5,000', '$6,000', '$6,000', 'Unknown', '$7,500', '$4,200'],
    'Join_Date': ['2023-01-15', '2023/02/20', '2023/02/20', '2024-03-01', 'Not Available', '2025-05-12']
}

df = pd.DataFrame(raw_data)
df = df.dropna(subset="Emp_ID")
df["Name"] = df["Name"].str.strip()
df["Department"] = df['Department'].str.strip()
df['Department'] = df['Department'].replace({"hr":"Human Resources",
                                             "it":"IT",
                                             "sales":"Sales",
                                             "HR":"Human Resources"})

df["Salary"] = df['Salary'].str.replace("$", "", regex=False).str.replace(",", "", regex=False)

df['Salary'] = pd.to_numeric(df['Salary'], errors="coerce")
df["Join_Date"] = pd.to_datetime(df["Join_Date"],errors="coerce",format="mixed")
meadian = df['Salary'].median()
df['Salary'] = df['Salary'].fillna(meadian)
df = df.drop_duplicates()
df = df.reset_index(drop=True)
# df = df.drop_duplicates(subset="Emp_ID")

print("--- final cleaned data ---")
print(df.to_string())
print("\n" + "="*40 + "\n")
