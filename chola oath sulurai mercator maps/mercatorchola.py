import requests
from PIL import Image

def crop_google_maps_image(google_maps_link, width, height):
  """Crops a Google Maps image completely and saves it as a high-quality lossless compression PNG image for the given width and height.

  Args:
    google_maps_link: The Google Maps website link to the image to be cropped.
    width: The width of the cropped image in square feet.
    height: The height of the cropped image in square feet.

  Returns:
    A PIL Image object of the cropped image.
  """

  # Get the Google Maps image.
  response = requests.get(google_maps_link)
  image = Image.open(response.content)

  # Calculate the crop coordinates.
  crop_coordinates = (0, 0, width * 1024, height * 1024)

  # Crop the image.
  cropped_image = image.crop(crop_coordinates)

  # Save the cropped image as a high-quality lossless compression PNG image.
  cropped_image.save(f"cropped_image_{width}_{height}.png", "PNG", lossless=True)

  return cropped_image

if __name__ == "__main__":
  # Get the Google Maps link to the image of India.
  google_maps_link = "https://www.google.com/maps/@23.746778,77.978169,10z"

  # Get the width and height of the cropped image in square feet.
  width = 10
  height = 10

  # Crop the Google Maps image and save it as a high-quality lossless compression PNG image.
  cropped_image = crop_google_maps_image(google_maps_link, width, height)

