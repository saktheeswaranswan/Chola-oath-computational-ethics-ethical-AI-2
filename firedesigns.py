import numpy as np
import matplotlib.pyplot as plt

# Create time intervals
t = np.linspace(0, 5, 100)  # Adjust time range and resolution as needed

# Define parameters for the shell burst
m_shell = 0.5  # Mass of the shell (in kg)
v_shell = 30.0  # Initial velocity of the shell (in m/s)
g = 9.81  # Acceleration due to gravity (in m/s^2)

# Calculate the height of the burst using kinematic equations
h = v_shell * t - 0.5 * g * t**2

# Plot the height-time graph
plt.plot(t, h)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Shell Burst Firework Effect')
plt.grid()

# Save the plot to a file
plt.savefig('shell_burst_firework.png')

# Show the plot (optional)
plt.show()

