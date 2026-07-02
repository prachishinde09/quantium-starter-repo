import pandas as pd

df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df1, df2, df3], ignore_index=True)

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Remove $ and convert price to float
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

# Calculate Sales
df["Sales"] = df["price"] * df["quantity"]

# Keep only required columns
df = df[["Sales", "date", "region"]]

# Rename columns
df.columns = ["Sales", "Date", "Region"]

# Save output
df.to_csv("formatted_sales_data.csv", index=False)

print(df.head())
print("Output file created successfully!")