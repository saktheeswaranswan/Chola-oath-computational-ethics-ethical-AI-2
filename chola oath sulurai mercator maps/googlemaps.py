import requests
from PIL import Image

def crop_google_maps_image(api_key, center, width, height, zoom):
    base_url = "https://maps.googleapis.com/maps/api/staticmap"
    
    # Define the parameters for the static map request.
    params = {
        "center": center,  # Coordinates of the center of the map (e.g., "23.746778,77.978169")
        "zoom": zoom,       # Zoom level (typically between 0 and 21)
        "size": f"{width}x{height}",  # Dimensions of the cropped image
        "key": api_key       # Your Google Cloud API key
    }

    # Send a GET request to the Static Maps API.
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Open and save the image.
        image = Image.open(BytesIO(response.content))
        image.save(f"cropped_image_{width}_{height}.png", "PNG")
        return image
    else:
        print(f"Error: Unable to fetch the map. Status code: {response.status_code}")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    center = "23.746778,77.978169"
    width = 640  # Adjust as needed
    height = 640  # Adjust as needed
    zoom = 10  # Adjust the zoom level as needed

    cropped_image = crop_google_maps_image(api_key, center, width, height, zoom)

