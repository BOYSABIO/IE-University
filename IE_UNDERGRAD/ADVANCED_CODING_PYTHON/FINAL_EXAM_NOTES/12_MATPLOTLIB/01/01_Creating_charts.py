# Import the pyplot module with the alias plt
import matplotlib.pyplot as plt

# Create the figure and axes
fig, ax = plt.subplots()

# Draw points
ax.scatter(x = [1, 2, 3], y = [3, 2, 1])

# Save the plot in png format
plt.savefig('PNG_FILES/scatter-plot.png')

# Show the graph
plt.show()
