import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
g = 0.81 # Acceleration due to gravity (m/s^2)

# Create a figure
fig, ax = plt.subplots()
ax.set_xlim(0, 50)
ax.set_ylim(0, 15)

# Create an empty line for the trajectory
line, = ax.plot([], [], 'ro')

# Function to initialize the plot
def init():
    line.set_data([], [])
    return line,

# Function to update the plot for each frame
def update(frame):
    # Calculate the trajectory for the given frame
    t = np.linspace(0, frame, 100)
    x = frame * np.cos(t)
    y = frame * np.sin(t) - 0.5 * g * t ** 2

    # Set the data for the line
    line.set_data(x, y)

    # Return the line
    return line,

# Animate the plot
ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)

# Keep the plot open until the user closes it
plt.show()

