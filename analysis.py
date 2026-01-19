import pandas as pd

df = pd.read_csv("rockstar_lifecycle_data.csv")

print(df)
print(df.info())
print(df.isna().sum())

# Convert year and duration columns to numeric
cols_to_convert = ["Release_Year", "Dev_Start_Year", "Dev_Duration_Years"]

for col in cols_to_convert:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print(df.dtypes)
import matplotlib.pyplot as plt

completed = df[df["Dev_Duration_Years"].notna()]

plt.figure()
plt.bar(completed["Game_Name"], completed["Dev_Duration_Years"])
plt.title("Rockstar Games – Development Duration Over Time")
plt.xlabel("Game Title")
plt.ylabel("Development Duration (Years)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("dev_duration.png")
plt.close()
df["Dev_Cost_USD_M"] = [5, 5, 12, 100, 265, 90, 185, 1500]
df["Revenue_USD_M"] = [300, 500, 850, 2000, 10000, 500, 5000, 3000]
plt.figure()
plt.scatter(df["Dev_Cost_USD_M"], df["Revenue_USD_M"])

for i, name in enumerate(df["Game_Name"]):
    plt.text(df["Dev_Cost_USD_M"][i], df["Revenue_USD_M"][i], name)

plt.title("Development Cost vs Revenue Scaling – Rockstar Games")
plt.xlabel("Development Cost (USD Million)")
plt.ylabel("Revenue (USD Million)")
plt.tight_layout()
plt.savefig("cost_vs_revenue.png")
plt.close()
df.to_csv("rockstar_lifecycle_cleaned.csv", index=False)

