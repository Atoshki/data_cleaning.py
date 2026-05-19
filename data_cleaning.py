import pandas as pd
import numpy as np

# Set seed for consistency
np.random.seed(2026)

practice_data = {
    'Employee_ID': [501, 502, 503, 504, 501, 505, 506, 507, 508, 509],
    'Full_Name': ['  tony STARK ', 'thor odinson', 'BRUCE BANNER', 'Natasha-Romanoff', '  tony STARK ', 'Steve R.', 'CLINT B.', 'wanda_maximoff', 'peter parker', 'Vision'],
    'Hire_Date': ['2024/01/10', '12-05-2024', '2024.08.15', '2024-11-01', '2024/01/10', np.nan, '02/28/2024', '2024-04-19', '2024/05/01', '2024-07-12'],
    'Monthly_Salary': ['$8,500.00', '9000', '$12,050.50', 'not_disclosed', '$8,500.00', '4500 dollars', '$15,000.00', '  $6000 ', np.nan, '$11,200.00'],
    'Performance_Score': [8.5, 9.0, -1.0, 7.5, 8.5, np.nan, 10.0, 6.5, 8.0, 9.5],
    'Department': ['tech', 'Tech', 'TECH', 'HR', 'tech', 'Operations', 'Ops', 'marketing', 'Marketing', 'mkt']
}

df = pd.DataFrame(practice_data)
striping = ["Full_Name","Hire_Date","Monthly_Salary","Department"]
for col in striping:
    df[col] = df[col].astype(str).str.strip()

df["Full_Name"] = df["Full_Name"].str.title()

df = df.drop_duplicates()

df["Performance_Score"] = df["Performance_Score"].clip(lower=0)
df["Performance_Score"] = pd.to_numeric(df["Performance_Score"], errors="coerce")

df["Hire_Date"] =pd.to_datetime(df["Hire_Date"], errors="coerce",format="mixed")

df["Monthly_Salary"] = df["Monthly_Salary"].str.replace(r"[\$,\s]|dollars","",regex=True)
df["Monthly_Salary"] = pd.to_numeric(df["Monthly_Salary"],errors="coerce")
median = df["Monthly_Salary"].median()
df["Monthly_Salary"] = df["Monthly_Salary"].fillna(median)

df["Department"] = df["Department"].str.lower()
df["Department"] = df["Department"].replace({"tech":"TECH",
                                             "hr":"Human Resources",
                                             "ops":"Operations",
                                             "operations":"Operations",
                                             "marketing":"Marketing",
                                             "mkt":"Marketing"})
# df = df.reset_index(drop=0)
print(df)
print("\n"+ "-"*100 + "\n")
