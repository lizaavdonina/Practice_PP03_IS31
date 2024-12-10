import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
from image_operations import ImageOperations

class ImageUtilityUI:
    def __init__(self, root):
        self.root = root
        self.image_ops = ImageOperations()

        self.root.title("Утилита работы с изображениями, практикант: Авдонина Елизавета Максимовна")

        self.load_button = tk.Button(root, text="Загрузить изображение", command=self.load_image)
        self.load_button.grid(row=0, column=0, padx=10, pady=10)

        self.resize_button = tk.Button(root, text="Изменить размер", command=self.resize_image)
        self.resize_button.grid(row=1, column=0, padx=10, pady=10)

        self.info_label = tk.Label(root, text="Информация об изображении:")
        self.info_label.grid(row=2, column=0, padx=10, pady=10)

        self.info_text = tk.Text(root, width=40, height=10)
        self.info_text.grid(row=3, column=0, padx=20, pady=20)

        self.image_label = tk.Label(root)
        self.image_label.grid(row=0, column=1, rowspan=4)

    def load_image(self):
        self.image_ops.load_image()
        if self.image_ops.image:
            self.display_image(self.image_ops.image)
            self.update_info()

    def resize_image(self):
        resized_image = self.image_ops.resize_image()
        if resized_image:
            self.display_image(resized_image)

    def display_image(self, img):
        img.thumbnail((400, 400))
        tk_image = ImageTk.PhotoImage(img)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image

    def update_info(self):
        self.info_text.delete(1.0, tk.END)
        if self.image_ops.image:
            width, height = self.image_ops.image.size
            self.info_text.insert(tk.END, f"Файл: {self.image_ops.image_path}\\n")
            self.info_text.insert(tk.END, f"Размер: {width}x{height}")
        else:
            self.info_text.insert(tk.END, "Изображение не загружено.")
