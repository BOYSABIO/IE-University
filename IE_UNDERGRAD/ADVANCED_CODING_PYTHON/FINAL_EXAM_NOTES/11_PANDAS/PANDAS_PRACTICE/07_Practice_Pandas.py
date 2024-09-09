"""The file titanic.csv contains information about the Titanic's passengers. Write a 
programwith the following requirements:
    1. Generate a DataFrame with the data in the file.
    2. Display the dimensions of the DataFrame, the number of data it contains, 
    thenames of its columns and rows, the data types of the columns, the first 10 rows
    and the last 10 rows.
    3. Display the passenger data with identifier 148.
    4. Display the even rows of the DataFrame.
    5. Display the names of the people who were in first class in alphabetical order.
    6. Display the percentage of people who survived and died.
    7. Display the percentage of people who survived in each class.
    8. Remove passengers with unknown age from the DataFrame.
    9. Add a new Boolean column to see if the passenger was a minor or not.
    10. Display the percentage of minors and seniors who survived in each class"""

import pandas as pd

#pd.set_option("display.max_columns", None)
#pd.set_option("display.max_rows", None)

df = pd.read_csv("CSV_FILES/titanic.csv", index_col = 0)
print(df)
print()

print("Dimensions: ", df.shape)
print("Name of Elements: ", df.size)
print("Column Name: ", df.columns)
print("Names of rows: ", df.index)
print("Datatypes: ", df.dtypes)
print("First 10 rows: ", df.head(10))
print("Last 10 rows: ", df.tail(10))
print()

print(df.loc[148])
print()

print(df.iloc[range(0, df.shape[0], 2)])
print(df.loc[::2])
print()

print(df.loc[df["Pclass"] == 1]["Name"].sort_values())
print()

print(df["Survived"].value_counts() / df["Survived"].count() * 100)
print()
print(df["Survived"].value_counts(normalize = True) * 100)
print()

print("Groupby")
print(df.groupby("Pclass")["Survived"].value_counts(normalize = True))
print()

print(df.dropna(subset = ["Age"]))
print()

df = df[df["Age"].notna()] #notna returns a df where all the values are replaced with boolean variable
print(df)
print()

df["Young"] = df["Age"] <= 18
print(df)
print()
print(df.groupby(["Pclass", "Young"])["Survived"].value_counts(normalize = True * 100))
