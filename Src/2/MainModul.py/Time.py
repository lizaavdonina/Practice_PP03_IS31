import tkinter as tk
from ui import ImageEditorApp
import time
import sys
import tracemalloc

def get_size(obj, seen=None):
    """Рекурсивно вычисляет размер объекта."""
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    size = sys.getsizeof(obj)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size

def main():
    # Начало мониторинга использования памяти
    tracemalloc.start()

    start_time = time.time()  # Начало замера времени

    root = tk.Tk()
    app = ImageEditorApp(root)

    end_time = time.time()  # Конец замера времени
    print(f"Time to create TK root and app: {end_time - start_time} seconds")

    # Получаем текущие затраты памяти
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage: {current / 1024} KB; Peak: {peak / 1024} KB")

    print(f"Size of root: {get_size(root)} bytes")
    print(f"Size of app: {get_size(app)} bytes")

    root.mainloop()

    # Завершаем мониторинг использования памяти
    tracemalloc.stop()

if __name__ == "__main__":
    main()
