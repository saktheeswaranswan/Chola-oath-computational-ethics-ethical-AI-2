import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create arrays to store data for each launch angle
x_data, y_data, z_data = [], [], []
launch_angles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Time step and total time
dt = 0.1
total_time = 10

# Number of time steps
num_steps = int(total_time / dt)

# Function to update and plot the trajectory for all launch angles
def update_trajectory(frame):
    global x_data, y_data, z_data

    # Clear previous data
    x_data, y_data, z_data = [], [], []

    for angle in launch_angles:
        # Initialize position and velocity for the current launch angle
        x, y, z = 0, 0, 0
        launch_angle_radians = np.radians(angle)
        vx = np.cos(launch_angle_radians)
        vy = np.sin(launch_angle_radians)
        vz = 10

        for _ in range(num_steps):
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

# Animate the trajectories for all launch angles simultaneously
ani = animation.FuncAnimation(fig, update_trajectory, frames=num_steps, repeat=False)

plt.show()

