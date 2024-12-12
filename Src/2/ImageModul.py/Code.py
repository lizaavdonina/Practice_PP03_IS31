from PIL import Image
class ImageProcessor:
    def __init__(self):
        self.image = None
    def load_image(self, path):
        self.image = Image.open(path)
    def resize_image(self, width, height):
        if self.image:
            self.image = self.image.resize((width, height))
    def rotate_image(self, angle):
        if self.image:
            self.image = self.image.rotate(angle, expand=True)
