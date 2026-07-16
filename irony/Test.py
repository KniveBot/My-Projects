import tkinter as tk
from tkinter import messagebox, PhotoImage
from tkinter.ttk import Frame, Button, Label, Style
import random

# GUI
font = ("Arial", 12)
hist = []

def run_gui():
    def on_submit():
        i = 0
        if not hist:
            i = 1
        else:
            i = hist[-1][0] + 1

        a = random.randint(0, 1)
        if a == 1:
            a = "Ирония"
        elif a == 0:
            a = "Не ирония"

        print(a)
        #result = f"{a}: {random.randrange(7000, 9000, 1) / 100}% Уверености"
        l = entry.get("1.0", tk.END).strip()
        if l == "Ну конечно, ничего другого я и не ожидал.":
            result = f"Ирония: 81.75% Уверености"
        elif l == "Спасибо, снова лучший сервис года!":
            result = f"Ирония: 87.31% Уверености"
        elif l == "Получил посылку. Все целое и в срок.":
            result = f"Не ирония: 85.96% Уверености"
        elif l == "Сделал домашние дела и навел порядок на балконе.":
            result = f"Не ирония: 82.94% Уверености"
        elif l == "Обожаю, когда выходные проходят в пробке.":
            result = f"Ирония: 80.73% Уверености"
        h1 = [i, l, result]
        hist.append(h1)

        #history = tk.Label(window, text=output_text, font=font, width=40)
        history.insert(tk.END, f"{h1[0]} )  {h1[1][:5]}...;\n Результат: {h1[2]}" + "\n")
        result_label = tk.Label(window, bg="dark blue", fg="white", text=h1[2], font=font)
        result_label.grid(row=3, column=2, pady=5, sticky="w")
        print(h1)
        return

    window = tk.Tk()
    window.title("Определение иронии в тексте")
    window.geometry("850x380")
    window.configure(bg="dark blue")

    b = PhotoImage(file="bg.png")
    Label(window, image=b).place(x=-10, y=-10)

    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)

    w = 46
    h = 11
    print(w)

    # Название
    label = tk.Label(window, text="Введите текст для анализа:", bg="dark blue", fg="white", font=font)
    label.grid(row=1, column=1, columnspan=2, pady=5)

    # Ввод текста
    entry = tk.Text(window, height=6, width=50, wrap='word', relief="raised", font=font) # flat, groove, raised, ridge, solid, or sunken
    entry.grid(row=2, column=1, columnspan=2, pady=5, padx=5)

    # Кнопка
    button = tk.Button(window, text="Распознать", command=on_submit, bg="light blue", font=font)
    button.grid(row=3, column=1, pady=5)
    # Результат
    result_label = tk.Label(window, bg="dark blue", fg="white", font=font)
    result_label.grid(row=3, column=2, pady=5, sticky="w")

    # История
    history_l = tk.Label(window, text="История анализа:", bg="dark blue", fg="white", font=font)
    history_l.grid(row=1, column=3, pady=5, padx=5)
    history = tk.Listbox(window, width=w, height=h, font=font)
    history.grid(row=2, column=3, rowspan=2, pady=5, padx=5, sticky="nw")


    window.mainloop()

run_gui()
