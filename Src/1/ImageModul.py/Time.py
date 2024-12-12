import time
import sys
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image

class ImageOperations:
    def __init__(self):
        self.image = None
        self.image_path = None

    def load_image(self):
        start_time = time.time()  # Начало измерения времени
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])

        if not self.image_path:
            return

        self.image = Image.open(self.image_path)
        end_time = time.time()  # Конец измерения времени

        # Вывод временных характеристик и размера image
        print(f"Время загрузки изображения: {end_time - start_time:.4f} секунд")
        print(f"Размер image: {sys.getsizeof(self.image)} байт")

    def resize_image(self):
        if self.image is None:
            messagebox.showwarning("Warning", "Сначала загрузите изображение")
            return None

        new_width = simpledialog.askinteger("Изменить размер", "Новая ширина:")
        new_height = simpledialog.askinteger("Изменить размер", "Новая высота:")

        if new_width is not None and new_height is not None:
            start_time = time.time()  # Начало измерения времени
            resized_image = self.image.resize((new_width, new_height), Image.LANCZOS)
            end_time = time.time()  # Конец измерения времени

            # Вывод временных характеристик и размера resized_image
            print(f"Время изменения размера изображения: {end_time - start_time:.4f} секунд")
            print(f"Размер resized_image: {sys.getsizeof(resized_image)} байт")

            return resized_image

        return None
