from PIL import Image
import os

# Directory containing image files
image_directory = "/home/josva/Documents/sujith/stimage"

# Get a list of image files in the directory
image_files = [f for f in os.listdir(image_directory) if f.endswith(('.jpg', '.jpeg', '.png'))]

# Sort the image files based on date modified
image_files.sort(key=lambda x: os.path.getmtime(os.path.join(image_directory, x)))

# Initialize variables for the final image width and height
final_width = 0
final_height = 0

images = []

# Load and process the images
for image_file in image_files:
    image_path = os.path.join(image_directory, image_file)
    img = Image.open(image_path)
    
    # Calculate the final height based on the tallest image
    final_height = max(final_height, img.height)
    
    # Add the image and its width to the list of images
    images.append((img, img.width))
    final_width += img.width

# Create a new blank image with the calculated dimensions
result_image = Image.new("RGB", (final_width, final_height))

# Paste each image side by side
x_offset = 0
for img, width in images:
    result_image.paste(img, (x_offset, 0))
    x_offset += width

# Save the stitched image
result_image.save("stitched_image.jpg")

print("Stitched image saved as stitched_image.jpg")

