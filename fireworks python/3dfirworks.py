import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create empty arrays for x, y, and z coordinates of the trajectory
x_data, y_data, z_data = [], [], []

# Create an initial position
x, y, z = 0, 0, 0

# Create an initial velocity
vx, vy, vz = 1, 1, 10

# Time step and total time
dt = 0.1
total_time = 10

# Number of time steps
num_steps = int(total_time / dt)

# Function to update the trajectory
def update_trajectory(frame):
    global x, y, z, vx, vy, vz

    # Update the position using the equations of motion
    x += vx * dt
    y += vy * dt
    z += vz * dt

    vz -= g * dt  # Update vertical velocity due to gravity

    x_data.append(x)
    y_data.append(y)
    z_data.append(z)

    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)
    ax.plot(x_data, y_data, z_data, 'r')

ani = animation.FuncAnimation(fig, update_trajectory, frames=num_steps, repeat=False)

plt.show()

