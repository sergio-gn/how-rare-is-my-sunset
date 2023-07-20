from flask import Flask, render_template, request
from PIL import Image
import webcolors

app = Flask(__name__)

def get_average_color(image_path):
    img = Image.open(image_path)
    img = img.resize((1, 1))  # Resize the image to 1x1 pixel to get the average color
    pixel = img.getpixel((0, 0))
    return pixel

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

@app.route('/', methods=['GET', 'POST'])
def index():
    color_code = None
    if request.method == 'POST':
        if 'file' in request.files:
            image_file = request.files['file']
            if image_file.filename != '':
                image_path = f"uploads/{image_file.filename}"
                image_file.save(image_path)
                average_color = get_average_color(image_path)
                color_code = rgb_to_hex(average_color)
    return render_template('index.html', color_code=color_code)

if __name__ == '__main__':
    app.run(debug=True)