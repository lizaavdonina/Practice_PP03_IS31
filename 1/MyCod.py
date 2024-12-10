import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk

class ImageUtilityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Утилита работы с изображениями, практикант: Авдонина Елизавета Максимовна")

        # Переменные для хранения изображения
        self.image = None
        self.image_path = None

        # Кнопки
        self.load_button = tk.Button(root, text="Загрузить изображение", command=self.load_image)
        self.load_button.grid(row=0, column=0, padx=10, pady=10)

        self.resize_button = tk.Button(root, text="Изменить размер", command=self.resize_image)
        self.resize_button.grid(row=1, column=0, padx=10, pady=10)

        # Блок информации
        self.info_label = tk.Label(root, text="Информация об изображении:")
        self.info_label.grid(row=2, column=0, padx=10, pady=10)

        self.info_text = tk.Text(root, width=40, height=10)
        self.info_text.grid(row=3, column=0, padx=20, pady=20)

        # Область для отображения изображения
        self.image_label = tk.Label(root)
        self.image_label.grid(row=0, column=1, rowspan=4)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if not self.image_path:
            return
        self.image = Image.open(self.image_path)
        self.display_image(self.image)
        self.update_info()

    def resize_image(self):
        if self.image is None:
            messagebox.showwarning("Warning", "Сначала загрузите изображение")
            return

        # Выбор новых размеров
        new_width = simpledialog.askinteger("Изменить размер", "Новая ширина:")
        new_height = simpledialog.askinteger("Изменить размер", "Новая высота:")

        if new_width is not None and new_height is not None:
            resized_image = self.image.resize((new_width, new_height), Image.LANCZOS)
            self.display_image(resized_image)

    def display_image(self, img):
        img.thumbnail((400, 400))  # Уменьшается изображение, если оно слишком большое
        self.tk_image = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.tk_image)
        self.image_label.image = self.tk_image

    def update_info(self):
        self.info_text.delete(1.0, tk.END)
        if self.image:
            width, height = self.image.size
            self.info_text.insert(tk.END, f"Файл: {self.image_path}\\n. ")
            self.info_text.insert(tk.END, f"Размер: {width}x{height}")
        else:
            self.info_text.insert(tk.END, "Изображение не загружено")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageUtilityApp(root)
    root.mainloop()
