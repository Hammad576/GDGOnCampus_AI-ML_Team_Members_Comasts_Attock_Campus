# %% Imports
import numpy as np
import pandas as pd

# ==========================================
# %% Assignment 1: DataFrame Creation and Indexing
# ==========================================

# 1. 4 columns, 6 rows random integers; set index to first column
data1_1 = np.random.randint(1, 100, size=(6, 4))
df1_1 = pd.DataFrame(data1_1, columns=['Col1', 'Col2', 'Col3', 'Col4'])
print("Assignment 1.1 - Original DataFrame:\n", df1_1)

df1_1_indexed = df1_1.set_index('Col1')
print("\nAssignment 1.1 - Indexed by Col1:\n", df1_1_indexed)

# 2. Columns 'A', 'B', 'C', index 'X', 'Y', 'Z'; access row 'Y', col 'B'
df1_2 = pd.DataFrame(
    np.random.randint(1, 50, size=(3, 3)),
    index=['X', 'Y', 'Z'],
    columns=['A', 'B', 'C']
)
print("\nAssignment 1.2 - DataFrame:\n", df1_2)
element = df1_2.loc['Y', 'B']
print(f"Element at row 'Y' and col 'B': {element}")


# ==========================================
# %% Assignment 2: DataFrame Operations
# ==========================================

# 1. Add new column that is the product of first two columns
df2_1 = pd.DataFrame(
    np.random.randint(1, 10, size=(5, 3)),
    columns=['Col1', 'Col2', 'Col3']
)
df2_1['Product'] = df2_1['Col1'] * df2_1['Col2']
print("\nAssignment 2.1 - DataFrame with Product column:\n", df2_1)

# 2. 4 rows, 3 columns; compute row-wise and column-wise sum
df2_2 = pd.DataFrame(
    np.random.randint(1, 20, size=(4, 3)),
    columns=['A', 'B', 'C']
)
print("\nAssignment 2.2 - DataFrame:\n", df2_2)
print("Row-wise sum (axis=1):\n", df2_2.sum(axis=1))
print("Column-wise sum (axis=0):\n", df2_2.sum(axis=0))


# ==========================================
# %% Assignment 3: Data Cleaning
# ==========================================

# 1. Introduce NaNs and fill with column mean
df3_1 = pd.DataFrame(
    np.random.randint(1, 50, size=(5, 3)).astype(float),
    columns=['A', 'B', 'C']
)
df3_1.iloc[0, 1] = np.nan
df3_1.iloc[2, 0] = np.nan
print("\nAssignment 3.1 - DataFrame with NaNs:\n", df3_1)

df3_1_filled = df3_1.fillna(df3_1.mean())
print("\nAssignment 3.1 - NaNs filled with column mean:\n", df3_1_filled)

# 2. Introduce NaNs and drop rows containing any NaN
df3_2 = pd.DataFrame(
    np.random.randint(1, 50, size=(6, 4)).astype(float),
    columns=['W', 'X', 'Y', 'Z']
)
df3_2.iloc[1, 2] = np.nan
df3_2.iloc[4, 0] = np.nan
print("\nAssignment 3.2 - DataFrame before dropping NaNs:\n", df3_2)

df3_2_dropped = df3_2.dropna()
print("\nAssignment 3.2 - After dropping rows with NaNs:\n", df3_2_dropped)


# ==========================================
# %% Assignment 4: Data Aggregation
# ==========================================

# 1. Group by 'Category' and calculate sum and mean of 'Value'
df4_1 = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=10),
    'Value': np.random.randint(10, 100, size=10)
})
print("\nAssignment 4.1 - DataFrame:\n", df4_1)
grouped4_1 = df4_1.groupby('Category')['Value'].agg(['sum', 'mean'])
print("\nAssignment 4.1 - Sum and Mean by Category:\n", grouped4_1)

# 2. Group by 'Category' and calculate total 'Sales'
df4_2 = pd.DataFrame({
    'Product': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6'],
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing', 'Home'],
    'Sales': np.random.randint(100, 1000, size=6)
})
print("\nAssignment 4.2 - Sales DataFrame:\n", df4_2)
total_sales = df4_2.groupby('Category')['Sales'].sum().reset_index()
print("\nAssignment 4.2 - Total Sales by Category:\n", total_sales)


# ==========================================
# %% Assignment 5: Merging DataFrames
# ==========================================

# 1. Merge two DataFrames on a common column ('ID')
df_left = pd.DataFrame({
    'ID': [101, 102, 103, 104],
    'Name': ['Ali', 'Bilal', 'Sara', 'Zain']
})
df_right = pd.DataFrame({
    'ID': [102, 103, 104, 105],
    'Score': [88, 92, 79, 85]
})
merged_df = pd.merge(df_left, df_right, on='ID', how='inner')
print("\nAssignment 5.1 - Merged on common column 'ID':\n", merged_df)

# 2. Concatenate along rows (axis=0) and along columns (axis=1)
df_a = pd.DataFrame({'Col1': [1, 2], 'Col2': [3, 4]})
df_b = pd.DataFrame({'Col3': [5, 6], 'Col4': [7, 8]})

concat_rows = pd.concat([df_a, df_b], axis=0, ignore_index=True)
concat_cols = pd.concat([df_a, df_b], axis=1)
print("\nAssignment 5.2 - Row-wise Concat:\n", concat_rows)
print("\nAssignment 5.2 - Column-wise Concat:\n", concat_cols)


# ==========================================
# %% Assignment 6: Time Series Analysis
# ==========================================

# 1. Datetime index, resample to monthly mean
dates6_1 = pd.date_range(start='2023-01-01', periods=100, freq='D')
df6_1 = pd.DataFrame({'Value': np.random.randint(10, 50, size=100)}, index=dates6_1)
monthly_mean = df6_1.resample('ME').mean()  # 'ME' represents month-end
print("\nAssignment 6.1 - Monthly Mean:\n", monthly_mean)

# 2. Date range 2021-01-01 to 2021-12-31, 7-day rolling mean
dates6_2 = pd.date_range(start='2021-01-01', end='2021-12-31', freq='D')
df6_2 = pd.DataFrame({'Value': np.random.randint(1, 100, size=len(dates6_2))}, index=dates6_2)
df6_2['Rolling_7D_Mean'] = df6_2['Value'].rolling(window=7).mean()
print("\nAssignment 6.2 - Rolling Mean (first 10 days):\n", df6_2.head(10))


# ==========================================
# %% Assignment 7: MultiIndex DataFrame
# ==========================================

# 1. MultiIndex DataFrame creation, indexing, and slicing
index7_1 = pd.MultiIndex.from_tuples([
    ('Dept_A', 'Emp_1'), ('Dept_A', 'Emp_2'),
    ('Dept_B', 'Emp_3'), ('Dept_B', 'Emp_4')
], names=['Department', 'Employee'])

df7_1 = pd.DataFrame(np.random.randint(50, 100, size=(4, 2)), index=index7_1, columns=['Score1', 'Score2'])
print("\nAssignment 7.1 - MultiIndex DataFrame:\n", df7_1)
print("Accessing Dept_A:\n", df7_1.loc['Dept_A'])
print("Accessing Dept_B -> Emp_3:\n", df7_1.loc[('Dept_B', 'Emp_3')])

# 2. MultiIndex ('Category', 'SubCategory') and aggregated sum
index7_2 = pd.MultiIndex.from_tuples([
    ('Food', 'Fruit'), ('Food', 'Snack'),
    ('Drink', 'Soda'), ('Drink', 'Juice')
], names=['Category', 'SubCategory'])

df7_2 = pd.DataFrame({'Sales': [150, 200, 80, 120]}, index=index7_2)
print("\nAssignment 7.2 - MultiIndex Sales:\n", df7_2)
print("Sum by Category:\n", df7_2.groupby(level='Category').sum())
print("Sum by SubCategory:\n", df7_2.groupby(level='SubCategory').sum())


# ==========================================
# %% Assignment 8: Pivot Tables
# ==========================================

# 1. Pivot table: Sum of 'Value' by 'Date' and 'Category'
df8_1 = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-01'],
    'Category': ['A', 'B', 'A', 'B', 'A'],
    'Value': [10, 20, 30, 40, 50]
})
pivot8_1 = df8_1.pivot_table(index='Date', columns='Category', values='Value', aggfunc='sum', fill_value=0)
print("\nAssignment 8.1 - Pivot Table (Sum by Date & Category):\n", pivot8_1)

# 2. Pivot table: Mean 'Revenue' by 'Quarter' and 'Year'
df8_2 = pd.DataFrame({
    'Year': [2022, 2022, 2022, 2023, 2023, 2023],
    'Quarter': ['Q1', 'Q2', 'Q1', 'Q1', 'Q2', 'Q2'],
    'Revenue': [1000, 1200, 1100, 1300, 1500, 1400]
})
pivot8_2 = df8_2.pivot_table(index='Year', columns='Quarter', values='Revenue', aggfunc='mean')
print("\nAssignment 8.2 - Pivot Table (Mean Revenue by Year & Quarter):\n", pivot8_2)


# ==========================================
# %% Assignment 9: Applying Functions
# ==========================================

# 1. Double the values of the DataFrame using applymap / map
df9_1 = pd.DataFrame(
    np.random.randint(1, 10, size=(5, 3)),
    columns=['C1', 'C2', 'C3']
)
print("\nAssignment 9.1 - Original:\n", df9_1)
df9_1_doubled = df9_1.map(lambda x: x * 2)
print("Doubled Values:\n", df9_1_doubled)

# 2. Add new column with the sum of all columns using a lambda function
df9_2 = pd.DataFrame(
    np.random.randint(1, 10, size=(6, 3)),
    columns=['ColA', 'ColB', 'ColC']
)
df9_2['Total'] = df9_2.apply(lambda row: row.sum(), axis=1)
print("\nAssignment 9.2 - Row Sum via Lambda:\n", df9_2)


# ==========================================
# %% Assignment 10: Working with Text Data
# ==========================================

# 1. Convert Series of strings to uppercase
text_series1 = pd.Series(['apple', 'banana', 'cherry', 'date', 'elderberry'])
print("\nAssignment 10.1 - Original Series:\n", text_series1)
print("Uppercase Series:\n", text_series1.str.upper())

# 2. Extract first 3 characters of each string
text_series2 = pd.Series(['python', 'pandas', 'numpy', 'scipy', 'matplotlib'])
print("\nAssignment 10.2 - Original Series:\n", text_series2)
print("First 3 characters extracted:\n", text_series2.str[:3])