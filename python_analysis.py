import numpy as np
import pandas as pd

# Sample dataset
data = {
    'TransactionID': [101, 102, 103, 104, 105, 105, 106, 107],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing', 'Clothing', 'Home', 'Electronics'],
    'UnitsSold': [2, 5, np.nan, 3, 4, 4, 1, 10],
    'UnitPrice': [1200, 450, 800, 250, np.nan, 450, 300, 1500],
    'Revenue': [2400, 2250, 1600, 750, 1800, 1800, 300, 15000]
}
df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False)

# 1. Load CSV and display basic info
df = pd.read_csv('sales_data.csv')
print("Basic Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# 2. Handle missing values and duplicates
df = df.drop_duplicates().reset_index(drop=True)
df['UnitsSold'] = df['UnitsSold'].fillna(df['UnitsSold'].median())
df['UnitPrice'] = df['UnitPrice'].fillna(df['UnitPrice'].median())

# 3. Group data by category and find total revenue
category_rev = df.groupby('Category')['Revenue'].sum().reset_index()
print("\nTotal Revenue by Category:")
print(category_rev)

# 4. Sort data by multiple columns
sorted_df = df.sort_values(by=['Category', 'Revenue'], ascending=[True, False])
print("\nSorted Data:")
print(sorted_df[['TransactionID', 'Category', 'Revenue']])

# 5. Correlation matrix for numerical columns
corr = df.select_dtypes(include=[np.number]).corr()
print("\nCorrelation Matrix:")
print(corr)