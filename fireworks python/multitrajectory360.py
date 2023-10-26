import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Time step and total time
dt = 0.1
total_time = 10

# Number of time steps
num_steps = int(total_time / dt)

# Generate launch angles from 10 to 100 degrees with a step of 1.1 degrees
launch_angles = np.arange(10, 100.1, 1.1)

# Create separate arrays to store data for each launch angle
x_data = []
y_data = []
z_data = []

# Function to update and plot the trajectory for a given launch angle
def update_trajectory(frame):
    # Clear the plot
    ax.clear()

    # Iterate through each launch angle and store data
    for angle in launch_angles:
        x_traj, y_traj, z_traj = [], [], []

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
            vz -= g * dt

            x_traj.append(x)
            y_traj.append(y)
            z_traj.append(z)

        # Append the trajectory data to the respective arrays
        x_data.append(x_traj)
        y_data.append(y_traj)
        z_data.append(z_traj)

    # Plot each trajectory with varying color and thickness
    for i in range(len(launch_angles)):
        color = plt.cm.viridis(i / len(launch_angles))
        linewidth = i / 10.0
        ax.plot(x_data[i], y_data[i], z_data[i], color=color, linewidth=linewidth)

# Animate the trajectories for all launch angles simultaneously
ani = animation.FuncAnimation(fig, update_trajectory, frames=num_steps, repeat=False)

plt.show()

