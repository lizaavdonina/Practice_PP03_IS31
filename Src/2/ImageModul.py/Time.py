import time
import sys
from PIL import Image

class ImageProcessor:
    def __init__(self):
        self.image = None

    def load_image(self, path):
        start_time = time.perf_counter()
        self.image = Image.open(path)
        end_time = time.perf_counter()
        mem_size = sys.getsizeof(self.image)
        print(f"Load image time: {end_time - start_time:.6f} seconds")
        print(f"Memory size of image: {mem_size} bytes")

    def resize_image(self, width, height):
        if self.image:
            start_time = time.perf_counter()
            self.image = self.image.resize((width, height))
            end_time = time.perf_counter()
            mem_size = sys.getsizeof(self.image)
            print(f"Resize image time: {end_time - start_time:.6f} seconds")
            print(f"Memory size after resize: {mem_size} bytes")

    def rotate_image(self, angle):
        if self.image:
            start_time = time.perf_counter()
            self.image = self.image.rotate(angle, expand=True)
            end_time = time.perf_counter()
            mem_size = sys.getsizeof(self.image)
            print(f"Rotate image time: {end_time - start_time:.6f} seconds")
            print(f"Memory size after rotate: {mem_size} bytes")
