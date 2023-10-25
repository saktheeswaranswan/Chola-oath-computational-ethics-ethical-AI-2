import pyautogui
import time

# Function to click coordinates in your browser and copy information
def click_coordinates_and_copy(x, y):
    # Click on the specified coordinates
    pyautogui.click(x, y)
    
    # Wait briefly for the information to load (you may need to adjust the sleep duration)
    time.sleep(2)
    
    # Select and copy the information (you may need to adjust the hotkey for copy)
    pyautogui.hotkey('ctrl', 'c')

# Replace these coordinates with the ones you want to click
x_coordinate = 100
y_coordinate = 100

# Call the function to click and copy
click_coordinates_and_copy(x_coordinate, y_coordinate)

# Now the information is copied to your clipboard, and you can paste it using 'ctrl + v' or pyautogui.hotkey('ctrl', 'v')

