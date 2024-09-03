# prompt: apply line plot in scatterplot

import matplotlib.pyplot as plt

# Generate some data
x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 2, 1]

# Create the plot
fig, ax = plt.subplots()

# Scatter plot
ax.scatter(x, y, color="red")

# Line plot
ax.plot(x, y, color="blue")

# Set labels and title
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_title("Scatter plot with line plot")
plt.show()
pip install geopandas matplotlib