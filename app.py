from flask import Flask, render_template, request
from PIL import Image
import os
import uuid
import threading
import time
import math
from io import BytesIO
import base64

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1500 * 1500  # 1MB in bytes

# Get the absolute path of the directory where app.py is located
current_directory = os.path.dirname(os.path.abspath(__file__))

def get_average_color(image_bytes):
    try:
        img = Image.open(image_bytes)
        img = img.resize((1, 1))  # Resize the image to 1x1 pixel to get the average color
        img_rgb = img.convert("RGB")
        pixel = img_rgb.getpixel((0, 0))
        return pixel  # Return the RGB tuple
    except (IOError, ValueError) as e:
        print(f"Error: {e}")
        return None

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])  # Format the RGB tuple directly

def delete_image(image_bytes):
    print(f"Deleting image...")
    # You can handle the image bytes here as needed without saving to the disk
    time.sleep(5)  # Sleep for 5 seconds to simulate image processing
    print(f"Image processing completed.")

def calculate_rgb_similarity(rgb1, rgb2):
    # Calculate Euclidean distance between two RGB colors
    return math.sqrt((rgb1[0] - rgb2[0])**2 + (rgb1[1] - rgb2[1])**2 + (rgb1[2] - rgb2[2])**2)

def get_color_range(rgb):
    total_pixels = 1  # For a single-pixel image

    if rgb[0] == rgb[1] == rgb[2]:  # If it's a grayscale color
        return "Neutral - 100%"

    # Define the common and rarest RGB spectra
    common_rgb = (101, 104, 146)
    rarest_rgb = (56, 39, 32)

    # Calculate the similarity between the image's RGB and the common and rarest RGB spectra
    similarity_to_common = calculate_rgb_similarity(rgb, common_rgb)
    similarity_to_rarest = calculate_rgb_similarity(rgb, rarest_rgb)

    # Determine the rarity based on the similarity
    if similarity_to_rarest <= 20:  # Adjust this threshold as needed
        return "Rare - less than 20%"
    elif similarity_to_common <= 45:  # Adjust this threshold as needed
        return "Uncommon - less than 45%"
    elif similarity_to_common <= 100:  # Adjust this threshold as needed
        return "Common"
    elif similarity_to_rarest <= 5:
        return "Super Rare - less than 5%"
    else:
        return "Legendary - less than 1%"

@app.route('/', methods=['GET', 'POST'])
def index():
    color_code = None
    image_data = None  # Variable to store the base64-encoded image data
    color_range = None  # Variable to store the color range text

    if request.method == 'POST':
        if 'file' in request.files:
            image_bytes = request.files['file'].read()  # Read the image as bytes

            average_color = get_average_color(BytesIO(image_bytes))  # Use BytesIO to handle the image as bytes

            if average_color:
                color_code = rgb_to_hex(average_color)
                color_range = get_color_range(average_color)

                # Convert the image bytes to base64-encoded string
                image_data = base64.b64encode(image_bytes).decode()

                # Schedule image processing as a background task
                processing_thread = threading.Thread(target=delete_image, args=[image_bytes])
                processing_thread.start()

    return render_template('index.html', color_code=color_code, image_data=image_data, color_range=color_range)

if __name__ == '__main__':
    app.run(debug=True)