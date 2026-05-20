import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data.csv")

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe(include="all"))

# Clean price column
df["Price"] = (
    df["Price"]
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .astype(float)
)

# Create graph
plt.figure(figsize=(10, 5))
sns.histplot(df["Price"], bins=10)

# Labels
plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Count")

# Show graph
plt.show()