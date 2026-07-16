import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

# Имя файла для сохранения обучающих примеров
TRAINING_FILE = "training_data.csv"

# Функция сохранения примера
def save_example():
    text = entry_text.get("1.0", tk.END).strip()
    label = label_var.get()
    if not text:
        messagebox.showwarning("Пустой ввод", "Введите текст фразы.")
        return

    # Загружаем текущие данные из файла
    if os.path.exists(TRAINING_FILE):
        df_existing = pd.read_csv(TRAINING_FILE)
    else:
        df_existing = pd.DataFrame(columns=["text", "label"])

    df_new = pd.DataFrame([{"text": text, "label": label}])
    df_all = pd.concat([df_existing, df_new], ignore_index=True)
    df_all.to_csv(TRAINING_FILE, index=False)

    messagebox.showinfo("Сохранено", "Фраза добавлена в набор для обучения.")
    entry_text.delete("1.0", tk.END)

# Интерфейс
root = tk.Tk()
root.title("Сбор обучающих примеров")

# Поле для ввода текста
tk.Label(root, text="Введите фразу:").pack(pady=5)
entry_text = tk.Text(root, height=4, width=60)
entry_text.pack()

# Переключатель ирония/не ирония
label_var = tk.IntVar()
label_var.set(0)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Radiobutton(frame, text="Не ирония", variable=label_var, value=0).pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame, text="Ирония", variable=label_var, value=1).pack(side=tk.LEFT, padx=10)

# Кнопка сохранить
tk.Button(root, text="Добавить в обучение", command=save_example).pack(pady=10)

root.mainloop()
