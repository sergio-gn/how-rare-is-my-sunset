# How Rare Is My Sunset?

## Overview

How rare is my sunset is a web application built using Flask that allows users to upload images and check how rare is their sunset based on a dataset of 150 sunsets taken on instagram. It iterates all the images using a thresold to select the most common and the rarest color result.
When you upload your picture you are comparing your result with the dataset results to find if it's closest to the rare spectrum os colors or if it's closest to the common spectrum. 
The application uses Python's PIL (Pillow) library to process the images and calculate the dominant color. Additionally, the application categorizes the extracted colors based on their rarity.

## Research Process

The research process involved identifying the best approach to extract the average color from images. The RGB value of the pixel at the center of the image was used as the average color. The rarity of the color was determined based on its similarity to common and rarest RGB spectra.

## Tools Used

- Flask: A lightweight web framework used to build the web application.
- PIL (Pillow): A Python Imaging Library used for image processing and color extraction.
- JavaScript: Used to display the filename on the custom file upload button.

## How to Use

### Clone the Repository

1. Open a terminal or command prompt.
2. Run the following command to clone the repository:

   ```bash
   git clone https://github.com/sergio-gn/how-rare-is-my-sunset.git

3. cd image-color-extractor
4. pip install -r requirements.txt
5. python app.py


#### How to Test
Upload an image using the "Upload Image" button.
The application will display the average color of the uploaded image and categorize it based on rarity.
#### Disclaimer
This is a robotic analysis. Please don't take this result seriously since robots see the world in numbers and humans see the world with senses and feelings! If you think your image is rare, it is!

License
This project is licensed under the MIT License - see the LICENSE file for details.