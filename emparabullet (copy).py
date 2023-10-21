import numpy as np
import matplotlib.pyplot as plt

# Define parameters
h1 = 0
v1 = 50
theta1_deg = 45
h2 = 0
v2 = 60
theta2_deg = 135
g = 9.81
air_resistance_coefficient = 0.01  # Air resistance coefficient
time_step = 0.01  # Time step for simulation

# Convert launch angles to radians
theta1_rad = np.radians(theta1_deg)
theta2_rad = np.radians(theta2_deg)

# Initialize lists to store the trajectory points
x1, y1, x2, y2 = [], [], [], []

# Initialize initial conditions
t = 0
x1.append(0)
y1.append(h1)
x2.append(0)
y2.append(h2)

# Simulation loop
while y1[-1] >= 0 and y2[-1] >= 0:
    # Calculate air resistance for both bullets
    air_resistance1 = air_resistance_coefficient * v1
    air_resistance2 = air_resistance_coefficient * v2

    # Update velocities with air resistance
    v1 -= air_resistance1 * v1 * time_step
    v2 -= air_resistance2 * v2 * time_step

    # Update positions
    x1.append(x1[-1] + v1 * np.cos(theta1_rad) * time_step)
    y1.append(y1[-1] + v1 * np.sin(theta1_rad) * time_step - 0.5 * g * time_step**2)
    x2.append(x2[-1] + v2 * np.cos(theta2_rad) * time_step)
    y2.append(y2[-1] + v2 * np.sin(theta2_rad) * time_step - 0.5 * g * time_step**2)
    t += time_step

# Plot the trajectories
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label="Bullet 1", color="red")
plt.plot(x2, y2, label="Bullet 2", color="blue")
plt.xlabel("Horizontal Position (m)")
plt.ylabel("Vertical Position (m)")
plt.legend()
plt.title("Projectile Motion of Bullets with Air Resistance")
plt.grid(True)
plt.show()

