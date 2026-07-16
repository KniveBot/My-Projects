import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

# Имя файла для сохранения обучающих примеров
TRAINING_FILE = "ruirony_combined_unique.csv"

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

    # Обновляем счётчик строк и меток
    count_label.config(text=f"Фраз в базе: {len(df_all)}")
    label_counts = df_all['label'].value_counts()
    count_0 = label_counts.get(0, 0)
    count_1 = label_counts.get(1, 0)
    label_stats.config(text=f"Не ирония (0): {count_0} | Ирония (1): {count_1}")

    messagebox.showinfo("Сохранено", "Фраза добавлена в набор для обучения.")
    entry_text.delete("1.0", tk.END)

# Интерфейс
root = tk.Tk()
root.title("Сбор обучающих примеров")
root.configure(bg="dark blue")

# Поле для ввода текста
tk.Label(root, text="Введите фразу:", bg="dark blue", fg="white").pack(pady=5)
entry_text = tk.Text(root, height=4, width=60)
entry_text.pack()

# Переключатель ирония/не ирония
label_var = tk.IntVar()
label_var.set(0)

frame = tk.Frame(root)
frame.pack(pady=5)
frame.configure(bg="dark blue")

tk.Radiobutton(frame, text="Не ирония", variable=label_var, value=0, bg="light blue").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame, text="Ирония", variable=label_var, value=1, bg="light blue").pack(side=tk.LEFT, padx=10)

# Кнопка сохранить
tk.Button(root, text="Добавить в обучение", bg="light blue", command=save_example).pack(pady=10)

# Метка количества строк и меток
if os.path.exists(TRAINING_FILE):
    df_initial = pd.read_csv(TRAINING_FILE)
    initial_count = len(df_initial)
    count_0 = df_initial['label'].value_counts().get(0, 0)
    count_1 = df_initial['label'].value_counts().get(1, 0)
else:
    initial_count = 0
    count_0 = 0
    count_1 = 0

count_label = tk.Label(root, text=f"Фраз в базе: {initial_count}", bg="light blue")
count_label.pack(pady=5)
label_stats = tk.Label(root, text=f"Не ирония (0): {count_0} | Ирония (1): {count_1}", bg="light blue")
label_stats.pack(pady=2)

root.mainloop()
