from tkinter import filedialog, messagebox, simpledialog
from PIL import Image

class ImageOperations:
    def __init__(self):
        self.image = None
        self.image_path = None

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if not self.image_path:
            return
        self.image = Image.open(self.image_path)

    def resize_image(self):
        if self.image is None:
            messagebox.showwarning("Warning", "Сначала загрузите изображение")
            return None

        new_width = simpledialog.askinteger("Изменить размер", "Новая ширина:")
        new_height = simpledialog.askinteger("Изменить размер", "Новая высота:")

        if new_width is not None and new_height is not None:
            return self.image.resize((new_width, new_height), Image.LANCZOS)
        return None
