import pandas as pd
df = pd.read_csv("dataset.csv")
print("Original Dataset:\n", df)
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)
df["Purchase"].fillna("No", inplace=True)
df.drop_duplicates(inplace=True)
df["Salary_Normalized"] = (
    (df["Salary"] - df["Salary"].min()) /
    (df["Salary"].max() - df["Salary"].min())
)
print("\nCleaned Dataset:\n", df)
df.to_csv("cleaned_dataset.csv", index=False)
print("\n Data cleaning completed. File saved as cleaned_dataset.csv")

