import os
from collections import Counter
from app import get_average_color, get_color_range

def get_images_in_folder(folder_path):
    image_paths = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            image_paths.append(image_path)
    return image_paths

def main():
    folder_path = './sunset_images'
    sunset_images = get_images_in_folder(folder_path)

    if not sunset_images:
        print("No valid images found in the folder.")
        return

    sunset_colors = []

    for image_path in sunset_images:
        average_color = get_average_color(image_path)
        if average_color:
            sunset_colors.append(average_color)

    color_counter = Counter(sunset_colors)

    # Sort colors by count in ascending order
    sorted_colors = color_counter.most_common()[::-1]

    rarest_color, rarest_count = sorted_colors[0]

    rarest_color_name = get_color_range(rarest_color)

    print(f"The most rare sunset color is: {rarest_color_name} - RGB: {rarest_color} - Count: {rarest_count}")

if __name__ == "__main__":
    main()