import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

print("Original Dataset:\n", df)

# -----------------------------
# 1. Handle Missing Values
# -----------------------------
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)
df["Purchase"].fillna("No", inplace=True)

# -----------------------------
# 2. Remove Duplicates
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# 3. Data Normalization (Salary scaling)
# -----------------------------
df["Salary_Normalized"] = (
    (df["Salary"] - df["Salary"].min()) /
    (df["Salary"].max() - df["Salary"].min())
)

print("\nCleaned Dataset:\n", df)

# Save cleaned file
df.to_csv("cleaned_dataset.csv", index=False)

print("\n✅ Data cleaning completed. File saved as cleaned_dataset.csv")
