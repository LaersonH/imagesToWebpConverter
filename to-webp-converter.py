import concurrent.futures
from PIL import Image
import os


def process_image(image):
    img = Image.open(f"before\\{str(image)}")
    image = image.split(".")
    img.save(f"afther\\{str(image[0])}.webp", format="WEBP")


if __name__ == '__main__':
    images = []
    for _, _, filenames in os.walk("before\\"):
        images = filenames
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, images)