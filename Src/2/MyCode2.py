import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Editor")

        # Инициализация переменных
        self.image_path = None
        self.image = None
        self.tk_image = None

        # Настройка интерфейса
        self.setup_ui()

    def setup_ui(self):
        # Панель с кнопками
        control_panel = tk.Frame(self.root)
        control_panel.pack(side=tk.LEFT, fill=tk.Y)

        # Кнопка загрузки изображения
        btn_load = tk.Button(control_panel, text="Загрузить изображение", command=self.load_image)
        btn_load.pack(padx=10, pady=5)

        # Поля для ширины и высоты
        self.width_var = tk.StringVar()
        self.height_var = tk.StringVar()

        tk.Label(control_panel, text="Ширина:").pack(padx=10, pady=5)
        tk.Entry(control_panel, textvariable=self.width_var).pack(padx=10, pady=5)

        tk.Label(control_panel, text="Высота:").pack(padx=10, pady=5)
        tk.Entry(control_panel, textvariable=self.height_var).pack(padx=10, pady=5)

        # Кнопка изменения размера
        btn_resize = tk.Button(control_panel, text="Изменить ширину и высоту", command=self.resize_image)
        btn_resize.pack(padx=10, pady=5)

        # Кнопка вращения изображения
        btn_rotate = tk.Button(control_panel, text="Повернуть изображение", command=self.rotate_image)
        btn_rotate.pack(padx=10, pady=5)

        # Метка для информации о действиях
        self.info_label = tk.Label(control_panel, text="", justify=tk.LEFT, wraplength=150)
        self.info_label.pack(padx=10, pady=5)

        # Канвас для отображения изображения
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if self.image_path:
            self.image = Image.open(self.image_path)
            self.display_image()
            self.info_label.config(text=f"Загружено: {self.image_path}")

    def display_image(self):
        if self.image is not None:
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
            self.canvas.config(width=self.image.width, height=self.image.height)

    def resize_image(self):
        if self.image is None:
            messagebox.showwarning("Предупреждение", "Сначала загрузите изображение.")
            return

        try:
            new_width = int(self.width_var.get())
            new_height = int(self.height_var.get())
            self.image = self.image.resize((new_width, new_height))
            self.display_image()
            self.info_label.config(text=f"Изменён размер: {new_width}x{new_height}")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные значения ширины и высоты.")

    def rotate_image(self):
        if self.image is None:
            messagebox.showwarning("Предупреждение", "Сначала загрузите изображение.")
            return

        self.image = self.image.rotate(90, expand=True)
        self.display_image()
        self.info_label.config(text="Изображение повернуто на 90 градусов")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEditorApp(root)
    root.mainloop()
