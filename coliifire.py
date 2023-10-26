import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define constants
g = 9.81  # Gravitational acceleration (m/s²)
rho = 1.225  # Air density at sea level (kg/m³)
Cd = 0.47  # Typical drag coefficient for a sphere
A = np.pi * (0.1**2)  # Cross-sectional area of the projectile (m²)
v0 = 100.0  # Initial velocity (m/s)
h0 = 0.0  # Initial height (m)
angles_deg = np.linspace(0, 90, 91)  # Launch angles (0 to 90 degrees)

# Define the equations of motion with air resistance
def projectile(t, u):
    x, y, vx, vy = u
    v = np.sqrt(vx**2 + vy**2)
    dxdt = vx
    dydt = vy
    dvxdt = -0.5 * rho * Cd * A * v * vx
    dvydt = -g - 0.5 * rho * Cd * A * v * vy
    return [dxdt, dydt, dvxdt, dvydt]

# Calculate and plot trajectories for various launch angles
for angle_deg in angles_deg:
    angle_rad = np.radians(angle_deg)
    initial_conditions = [0, h0, v0 * np.cos(angle_rad), v0 * np.sin(angle_rad)]
    sol = solve_ivp(projectile, [0, 100], initial_conditions, t_eval=np.linspace(0, 100, 1000), vectorized=True)

    # Extract trajectory data
    x = sol.y[0]
    y = sol.y[1]

    # Plot the trajectory
    plt.plot(x, y, label=f'{angle_deg}°')

plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.title('Projectile Motion with Air Resistance')
plt.legend()
plt.grid()
plt.show()

