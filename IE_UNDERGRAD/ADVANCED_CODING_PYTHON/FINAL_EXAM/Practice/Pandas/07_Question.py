"""The file titanic.csv contains information about the Titanic's passengers. Write a program with the following 
requirements:
    1. Generate a DataFrame with the data in the file.
    2. Display the dimensions of the DataFrame, the number of data it contains, the names of its columns and rows, 
        the data types of the columns, the first 10 rowsand the last 10 rows.
    3. Display the passenger data with identifier 148.
    4. Display the even rows of the DataFrame.
    5. Display the names of the people who were in first class in alphabetical order.
    6. Display the percentage of people who survived and died.
    7. Display the percentage of people who survived in each class.
    8. Remove passengers with unknown age from the DataFrame.
    9. Display by screen the average age of the women who traveled in each class.
    10. Add a new Boolean column to see if the passenger was a minor or not.
    11. Display the percentage of minors and seniors who survived in each class."""

import pandas as pd

# Generate a DataFrame with the data in the file
df = pd.read_csv("CSV_FILES/titanic.csv", index_col = 0)
print(df)
print()

# Display the dimensions of the Dataframe, the number of data it contains, the names of its columns and rows, the data types of the columns, the first 10 rows and the last 10 rows
print("The dataframe has", df.shape[0], "rows and", df.shape[1], "columns.")
print()

print("The Dataframe contains", df.size, "data")
print()

print("Column Names: ", df.columns)
print("Row Names: ", df.index)
print()

print("Datatypes:\n", df.dtypes)
print()

print("First 10 Rows:\n", df.head(10))
print("Last 10 Rows:\n", df.tail(10))
print()

# Display the passenger data with identifier 148
print(df.loc[148])
print()

# Display the even rows of the DataFrame
print(df.iloc[range(0, df.shape[0], 2)])
print()

# Display the names of the people who were in first class in alphabetical order
print(df[df["Pclass"] == 1]["Name"].sort_values())
print()

# Display the percentage of people who survived and died
print(df["Survived"].value_counts(normalize = True) * 100)
print()

# Display the percentage of people who survived in each class
print(df.groupby("Pclass")["Survived"].value_counts(normalize = True) * 100)
print()

# Remove passengers with unknown age from the DataFrame
print(df.dropna(subset = ['Age']))
print()

# Display by screen the average age of the women who traveled in each class
print(df.groupby(['Pclass', 'Gender'])['Age'].mean().unstack()['female'])
print()

# Add a new Boolean column to see if the passenger was a minor or not
df['Minor'] = df['Age'] < 18
print(df)
print()

# Display the percentage of minors and seniors who survived in each class
print(df.groupby(["Pclass", "Minor"])["Survived"].value_counts(normalize = True) * 100)
print()