import tkinter as tk
from ui import ImageUtilityUI
import time
import sys

def print_sys_info():
    print("Размер используемой памяти:", sys.getsizeof(sys))
    print("Размер используемых объектов root:", sys.getsizeof(root))
    print("Размер используемых объектов app:", sys.getsizeof(app))

if __name__ == "__main__":
    # Измерение времени выполнения создания основного окна
    start_time = time.time()
    root = tk.Tk()
    creation_time = time.time() - start_time
    print(f"Время создания root: {creation_time:.6f} секунд")

    # Измерение времени выполнения инициализации приложения
    start_time = time.time()
    app = ImageUtilityUI(root)
    initialization_time = time.time() - start_time
    print(f"Время инициализации приложения: {initialization_time:.6f} секунд")

    # Печать информации о памяти
    print_sys_info()

    # Измерение времени выполнения главного цикла
    start_time = time.time()
    root.mainloop()
    mainloop_time = time.time() - start_time
    print(f"Время выполнения главного цикла: {mainloop_time:.6f} секунд")
