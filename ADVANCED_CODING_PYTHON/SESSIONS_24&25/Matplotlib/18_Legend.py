import matplotlib.pyplot as plt

fig, ax = plt.subplots()
days = ['M', 'T', 'W', 'Th', 'F', 'S', 'Su']
temperatures = {'Madrid':[28.5, 30.5, 31, 30, 30, 28, 27.5], 'Barcelona':[24.5, 25.5, 26.5, 26.5, 25, 26.5, 24.5]}
ax.plot(days, temperatures['Madrid'], label = 'Madrid')
ax.plot(days, temperatures['Barcelona'], label = 'Barcelona')
ax.legend(loc = 'upper right')

plt.show()