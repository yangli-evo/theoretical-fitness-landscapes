import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Generate data for the fitness landscape
x = np.linspace(0, 1, 50)  # X coordinates
y = np.linspace(0, 1, 50)  # Y coordinates
x, y = np.meshgrid(x, y)    # Create grid of X, Y coordinates

# Define a single-peaked fitness function (example)
z = np.exp(-((x - 0.5)**2 + (y - 0.5)**2) / 0.1)  # Example of a single-peaked function

# Plotting the 3D surface
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Add labels and title
ax.set_xlabel('Genotype X')
ax.set_ylabel('Genotype Y')
ax.set_zlabel('Fitness')
ax.set_title('Single-Peaked 3D Fitness Landscape')

plt.savefig('single_peaked_fitness_landscape.pdf', format='pdf')

# Show plot
plt.show()

