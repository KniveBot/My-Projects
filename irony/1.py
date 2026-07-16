import tkinter as tk
import threading
import time
import random

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Постоянно Пополняющийся Список")

        self.listbox = tk.Listbox(root, width=50, height=20)  # Создаем Listbox
        self.listbox.pack(pady=10)

        self.stop_flag = threading.Event()  # Флаг для остановки потока

        self.add_button = tk.Button(root, text="Добавить элемент", command=self.add_item)
        self.add_button.pack()

        self.start_button = tk.Button(root, text="Запустить поток", command=self.start_thread)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Остановить поток", command=self.stop_thread)
        self.stop_button.pack()

        self.data_thread = None # Храним ссылку на поток

    def add_item(self):
        """Добавляет элемент в список."""
        new_item = f"Элемент {random.randint(1, 1000)}"  # Создаем новый элемент
        self.listbox.insert(tk.END, new_item)  # Добавляем элемент в Listbox
        self.listbox.see(tk.END)  # Прокручиваем Listbox к последнему элементу

    def worker_thread(self):
        """Функция, выполняющаяся в отдельном потоке и добавляющая элементы."""
        while not self.stop_flag.is_set():  # Пока флаг остановки не установлен
            self.root.after(0, self.add_item)  # Добавляем задачу в главный поток Tkinter
            time.sleep(1)  # Пауза в 1 секунду

    def start_thread(self):
        """Запускает поток, добавляющий элементы в список."""
        if self.data_thread is None or not self.data_thread.is_alive(): # Проверяем, что поток не запущен
            self.stop_flag.clear() # Сбрасываем флаг остановки
            self.data_thread = threading.Thread(target=self.worker_thread, daemon=True)
            self.data_thread.start()
            print("Поток запущен")
        else:
            print("Поток уже запущен")

    def stop_thread(self):
        """Останавливает поток, добавляющий элементы в список."""
        self.stop_flag.set()  # Устанавливаем флаг остановки
        if self.data_thread and self.data_thread.is_alive():
            self.data_thread.join() # Дожидаемся завершения потока
        print("Поток остановлен")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
