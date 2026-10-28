import pandas as pd
import numpy as np

#-------------------------------------------------------------
#----------Task 1: DtaFrame Creation and indecxing------------
#-------------------------------------------------------------

df1 = pd.DataFrame(np.random.randint(1, 100, size=(6, 4)),
                  columns=['A', 'B', 'C', 'D'])
print("Original DataFrame:\n", df1)

# Set the first column as the index
df1 = df1.set_index('A')
print("DataFrame with 'A' as index:\n", df1)

#---------------------Part 2-----------------------------------
#DataFrame with column 'X', 'Y', 'Z' and index 'A', 'B', 'C'
df2 = pd.DataFrame(np.random.randint(1, 50, size=(3, 3)),
                  index=['A', 'B', 'C'],
                  columns=['X', 'Y', 'Z'])
print("DataFrame 2:\n", df2)
#Access the value at row 'B' and column 'Y'
value = df2.loc['B', 'Y']
print("Value at row 'B' and column 'Y':", value)



#-------------------------------------------------------------
#--------------Task 2: DataFrame Operations-------------------
#-------------------------------------------------------------
df3 = pd.DataFrame(np.random.randint(1, 20, size=(3, 5)),
                  columns=['P', 'Q', 'R', 'S', 'T'])
print("DataFrame 3:\n", df3)
#New column as product of columns 'P' and 'Q'
df3['Product_PQ'] = df3['P'] * df3['Q']
print("DataFrame 3 with new column:\n", df3)

#--------------------Part 2-----------------------------------
df4 = pd.DataFrame(np.random.randint(1, 30, size=(3, 4)),
                    columns=['M', 'N', 'O', 'P'])
print("DataFrame 4:\n", df4)
#Calculate the sum of each column
column_sums = df4.sum()
print("Column sums:\n", column_sums)
#Calculate the sum of each row
row_sums = df4.sum(axis=1)
print("Row sums:\n", row_sums)



#-------------------------------------------------------------
#----------------Task 3: DataFrame Cleaning-------------------
#-------------------------------------------------------------
df5 = pd.DataFrame(np.random.randint(1, 100, size=(3, 5)),
                  columns=['A', 'B', 'C', 'D', 'E'])
print("DataFrame 5:\n", df5)
#Replace values greater than 50 with NaN
df5[df5 > 50] = np.nan
print("DataFrame 5 after replacing values > 50 with NaN:\n", df5)
#Fill Nan values with the mean of each column
df5.fillna(df5.mean(), inplace=True)
print("DataFrame 5 after filling NaN values with column means:\n", df5)


#--------------------Part 2-----------------------------------
df6 = pd.DataFrame(np.random.randint(1, 100, size=(4, 6)),
                    columns=['A', 'B', 'C', 'D', 'E', 'F'])
print("DataFrame 6:\n", df6)
#Replace values greater than 70 with NaN
df6[df6 > 70] = np.nan
print("DataFrame 6 after replacing values > 70 with NaN:\n", df6)
#Drop the row having Nan values
df6.dropna(inplace=True)
print("DataFrame 6 after dropping rows with NaN values:\n", df6)



#-------------------------------------------------------------
#----------------Task 4: Data Aggregation---------------------
#-------------------------------------------------------------
df = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C'], size=10),
    'Value': np.random.randint(1, 100, size=10)
})
print("DataFrame:\n", df)

result = df.groupby('Category')['Value'].agg(['sum', 'mean'])
print("Sum and mean per category:\n", result)


#--------------------Part 2-----------------------------------
df7 = pd.DataFrame({
    'Category': np.random.choice(['X', 'Y', 'Z'], size=12),
    'Value': np.random.randint(1, 100, size=12),
    'sales': np.random.randint(1, 100, size=12)
})
#group by category and compute total sales of each category
result = df7.groupby('Category')['sales'].sum()
print("Total sales per category:\n", result)



#-------------------------------------------------------------
#----------------Task 5: Merging and Joining------------------
#-------------------------------------------------------------
df8 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})
df9 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Age': [25, 30, 35, 40]
})

#Merge the two DataFrames on 'ID'
merged_df = pd.merge(df8, df9, on='ID', how='inner')
print("Merged DataFrame:\n", merged_df)


#--------------------Part 2-----------------------------------
df10 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})
print("DataFrame 10:\n", df10)
df11 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Age': [25, 30, 35, 40]
})
print("DataFrame 11:\n", df11)

#Concatenate using row and coloumn-wise
concatenated_row = pd.concat([df10, df11], axis=0, ignore_index=True)
print("Row-wise concatenated DataFrame:\n", concatenated_row)



#---------------------------------------------------------------
#----------------Task 6: Time series analysis-------------------
#---------------------------------------------------------------
dates = pd.date_range(start='2021-01-01', end='2021-12-31', freq='D')
df12 = pd.DataFrame(np.random.randint(1, 100, size=len(dates)),
                  index=dates, columns=['Value'])
print("DataFrame:\n", df12.head())

# 'ME' = month end (use 'M' on older pandas versions)
monthly_mean = df12.resample('ME').mean()
print("Monthly mean:\n", monthly_mean)


#--------------------Part 2-----------------------------------
dates = pd.date_range(start='2021-01-01', end='2021-12-31')
df13 = pd.DataFrame(np.random.randint(1, 100, size=len(dates)),
                  index=dates, columns=['Value'])

df13['Rolling_Mean'] = df13['Value'].rolling(window=7).mean()
print(df13.head(10))



#---------------------------------------------------------------
#-------------Task 7: MultiIndex dataframe----------------------
#---------------------------------------------------------------
# Create a MultiIndex DataFrame
index = pd.MultiIndex.from_product([['A', 'B'], [1, 2, 3]],
                                   names=['Letter', 'Number'])
df14 = pd.DataFrame(np.random.randint(1, 100, size=(6, 2)),
                  index=index, columns=['X', 'Y'])
print("MultiIndex DataFrame:\n", df14)
# All rows of the outer level 'A'
print("Rows for 'A':\n", df14.loc['A'])
# A single row using both levels
print("Row ('B', 2):\n", df14.loc[('B', 2)])
# One column for a specific outer level
print("Column X for 'A':\n", df14.loc['A', 'X'])
# Cross-section: all rows where the inner level is 2
print("Number = 2 across all letters:\n", df14.xs(2, level='Number'))
# Slicing a range of the inner level
print("Slice:\n", df14.loc[('A', 1):('B', 1)])


#--------------------Part 2-----------------------------------
index = pd.MultiIndex.from_product(
    [['Electronics', 'Clothing'], ['Sub1', 'Sub2']],
    names=['Category', 'SubCategory'])

# Repeat each combination so there are several values per group
index = index.repeat(3)
df15 = pd.DataFrame({'Value': np.random.randint(1, 100, size=len(index))},
                  index=index)
print("DataFrame:\n", df15)

# Sum for each Category and SubCategory
result = df15.groupby(level=['Category', 'SubCategory']).sum()
print("Sum per Category and SubCategory:\n", result)



#---------------------------------------------------------------
#----------------Task 8: Pivot tables---------------------------
#---------------------------------------------------------------
df16 = pd.DataFrame({
    'category': np.random.choice(['A', 'B', 'C'], size=10),
    'value1': np.random.randint(1, 100, size=10),
    'Date': pd.date_range(start='2021-01-01', periods=10, freq='D')
})
print("DataFrame:\n", df16)
#Sum of value for each category by date
pivot_table = df16.pivot_table(values='value1', index='Date', columns='category', aggfunc='sum', fill_value=0)
print("Pivot Table:\n", pivot_table)


#--------------------Part 2-----------------------------------
df17 = pd.DataFrame({
    'year': np.random.choice([2020, 2021], size=12),
    'quarter': np.random.choice([1, 2, 3, 4], size=12),
    'revenue': np.random.randint(1000, 5000, size=12)
})
print("DataFrame:\n", df17)
#Create a pivot table to show mean revenue for each quarter by year
pivot_table = df17.pivot_table(values='revenue', index='year', columns='quarter', aggfunc='mean', fill_value=0)
print("Pivot Table:\n", pivot_table)



#--------------------------------------------------------------
#----------------Task 9: Applying Functions -------------------
#--------------------------------------------------------------
df18 = pd.DataFrame(np.random.randint(1, 20, size=(5, 3)),
                  columns=['A', 'B', 'C'])
print("Original DataFrame:\n", df18)
def double(x):
    return x * 2
doubled = df18.apply(double)
print("Doubled DataFrame:\n", doubled)

#--------------------Part 2-----------------------------------
df19 = pd.DataFrame(np.random.randint(1, 50, size=(3, 6)),
                  columns=['U', 'V', 'W', 'X', 'Y', 'Z'])
print("DataFrame:\n", df19)
#Apply lambda function to calculate sum of column as a new column
df19['Sum'] = df19.apply(lambda x: x.sum(), axis=1)
print("DataFrame with Sum Column:\n", df19)




#---------------------------------------------------------------
#----------------Task 10: Working with text data----------------
#---------------------------------------------------------------
#Create panadas series with 5 random text strings
text_series = pd.Series(['apple', 'banana', 'cherry', 'date', 'elderberry'])
print("Original Series:\n", text_series)
#Convert all strings to uppercase
upper_series = text_series.str.upper()
print("Uppercase Series:\n", upper_series)


#--------------------Part 2-----------------------------------
text_series2 = pd.Series(['hello world', 'pandas is great', 'data science', 'machine learning', 'python programming'])
print("Original Series:\n", text_series2)
#Extract the first 3 characters of each string
first_three_chars = text_series2.str[:3]
print("First three characters:\n", first_three_chars)