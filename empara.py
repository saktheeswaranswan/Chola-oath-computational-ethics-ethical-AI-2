def calculate_interception_time(target_position, interceptor_speed):
    time_to_intercept = target_position / interceptor_speed
    return time_to_intercept

# Define parameters
target_position = 10000  # Initial distance to the target (meters)
interceptor_speed = 2500  # Interceptor missile speed (m/s)

# Calculate time to intercept
interception_time = calculate_interception_time(target_position, interceptor_speed)

print(f"Time to Intercept: {interception_time} seconds")

