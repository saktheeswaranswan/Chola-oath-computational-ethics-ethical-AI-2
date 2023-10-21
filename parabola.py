import numpy as np
import matplotlib.pyplot as plt

# Define parameters
h1 = 0.0  # Initial height of the first bullet's muzzle (meters)
v1 = 50.0  # Initial velocity of the first bullet (m/s)
theta1 = 45.0  # Launch angle of the first bullet (degrees)

h2 = 0.0  # Initial height of the second bullet's muzzle (meters)
v2 = 60.0  # Initial velocity of the second bullet (m/s)
theta2 = 30.0  # Launch angle of the second bullet (degrees)

g = 9.81  # Acceleration due to gravity (m/s^2)
air_resistance_coefficient = 0.01  # Air resistance coefficient

# Convert launch angles to radians
theta1_rad = np.radians(theta1)
theta2_rad = np.radians(theta2)

# Time step for numerical integration
dt = 0.01  # Adjust the time step as needed

# Initialize lists to store the trajectory points
x1, y1, x2, y2 = [], [], [], []

# Initialize initial conditions
t = 0
x1.append(0)
y1.append(h1)
x2.append(0)
y2.append(h2)

while y1[-1] >= 0 and y2[-1] >= 0:
    # Calculate air resistance for both bullets
    air_resistance1 = air_resistance_coefficient * v1
    air_resistance2 = air_resistance_coefficient * v2

    # Update velocities with air resistance
    v1 -= air_resistance1 * v1 * dt
    v2 -= air_resistance2 * v2 * dt

    # Update positions
    x1.append(x1[-1] + v1 * np.cos(theta1_rad) * dt)
    y1.append(y1[-1] + v1 * np.sin(theta1_rad) * dt - 0.5 * g * dt**2)
    x2.append(x2[-1] + v2 * np.cos(theta2_rad) * dt)
    y2.append(y2[-1] + v2 * np.sin(theta2_rad) * dt - 0.5 * g * dt**2)
    t += dt

# Find the time of intersection
t_intersection = t

# Plot the trajectories
plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label="Bullet 1", color="red")
plt.plot(x2, y2, label="Bullet 2", color="blue")
plt.scatter(x1[-1], y1[-1], color="green", marker="o", label="Intersection")
plt.xlabel("Horizontal Position (m)")
plt.ylabel("Vertical Position (m)")
plt.legend()
plt.title("Projectile Motion of Bullets with Air Resistance")
plt.grid(True)
plt.show()

