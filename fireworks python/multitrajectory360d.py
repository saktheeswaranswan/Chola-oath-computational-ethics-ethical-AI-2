import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Scale

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create arrays to store data for a single launch angle
x_data, y_data, z_data = [], [], []

# Time step and total time
dt = 0.1
total_time = 10

# Number of time steps
num_steps = int(total_time / dt)

# Function to update and plot the trajectory for a given launch angle
def update_trajectory(launch_angle_degrees):
    x_data, y_data, z_data = [], [], []

    # Initialize position and velocity for the current launch angle
    x, y, z = 0, 0, 0
    launch_angle_radians = np.radians(launch_angle_degrees)
    vx = np.cos(launch_angle_radians)
    vy = np.sin(launch_angle_radians)
    vz = 10

    for _ in range(num_steps):
        # Update the position using the equations of motion
        x += vx * dt
        y += vy * dt
        z += vz * dt
        vz -= g * dt

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

# Create a tkinter window
root = tk.Tk()
root.title("Parabolic Trajectory Animation")

# Create a Scale widget (slider) to control the launch angle
slider = Scale(root, from_=0, to=360, orient='horizontal', label='Launch Angle (degrees)', length=400, resolution=0.1)
slider.set(45)  # Set the initial value

# Function to update the trajectory when the slider value changes
def on_slider_change(val):
    launch_angle = slider.get()
    update_trajectory(launch_angle)
    canvas.draw()

# Attach the slider's event handler
slider.config(command=on_slider_change)
slider.pack()

# Create a canvas to display the matplotlib figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Initialize the trajectory with the initial launch angle
update_trajectory(slider.get())

root.mainloop()

