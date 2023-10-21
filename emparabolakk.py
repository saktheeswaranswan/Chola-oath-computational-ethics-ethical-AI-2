import matplotlib.pyplot as plt
import numpy as np

def missile_trajectory(target_position, interceptor_speed, total_time):
    times = np.linspace(0, total_time, num=100)
    positions = interceptor_speed * times
    return times, positions

# Define parameters
target_position = 10000  # Initial distance to the target (meters)
interceptor_speed = 2500  # Interceptor missile speed (m/s)

# Calculate time to intercept
interception_time = target_position / interceptor_speed

# Simulate missile trajectory
total_time = interception_time
times, positions = missile_trajectory(target_position, interceptor_speed, total_time)

# Plot the missile trajectory
plt.figure(figsize=(10, 6))
plt.plot(times, positions, label="Interceptor Missile", color="blue")
plt.xlabel("Time (seconds)")
plt.ylabel("Position (meters)")
plt.axvline(x=interception_time, color="red", linestyle="--", label="Interception Time")
plt.legend()
plt.title("Interceptor Missile Trajectory")
plt.grid(True)
plt.show()

print(f"Time to Intercept: {interception_time} seconds")

