import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_dataset.csv")

plt.hist(df["Age"])
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.boxplot(df["Salary"])
plt.title("Salary Boxplot")
plt.show()

