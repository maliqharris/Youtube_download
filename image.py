import requests
from PIL import Image
from io import BytesIO
import sys
import os

def show_thumbnail(image_url):
    # Fetch the image from the URL
    response = requests.get(image_url)
    
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))

        # Save the image to a temporary file
        temp_path = "temp_image.png"
        img.save(temp_path)

        # Print the escape code for image display in iTerm2
        print(f"\033]1337;File=inline=1:{os.path.abspath(temp_path)}\a")
    else:
        print("Failed to fetch the image.")

