import pandas as pd
import matplotlib.pyplot as plt

data = {
    'calories':[420, 380, 390, 490, 300],
    'time':[60, 40, 75, 55, 45]
}

# Create the following Dataframe
df = pd.DataFrame(data, index = ['L', 'M', 'X', 'J', 'V'])
print(df)

# Calculate the mean, median, and standard deviation
print(df['calories'].mean())
print(df['time'].mean())
print()

print(df['calories'].median())
print(df['time'].median())
print()

print(df['calories'].std())
print(df['time'].std())
print()

# Add another boolean column to the dataframe to see if the challenge of burning more than 400 calories
# per hour has been met. The new column should be generated by applying a formula to the other columns
#df["goal_met"] = (df['calories'] > 400) & (df['time'] <= 60)
#print(df)

print(400/60)

df['goal_met'] = (df['calories'] / df['time']) > 400 / 60
print(df)
print()

# Filter the Dataframe and return another dataframe with the even rows that satisfy that the
# number of calories is greater thatn 400
df1 = df.iloc[range(0, df.shape[0], 2)]
print(df1[df1['calories'] > 400])

# Create from the dataframe a series with the percentages of days that the challenge was achieved
# and those that were not
series = pd.Series(df['goal_met'].value_counts(normalize = True))
print(series)

# Create a graph like the one below showing the progression of calories and time during week
fig, ax = plt.subplots()
ax.plot(df['calories'])
ax.plot(df['time'])
ax.set_title('Calories & Time Progression', loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
plt.show()