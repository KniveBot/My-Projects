import tkinter as tk
from tkinter import messagebox
import os
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Проверка наличия модели
if not os.path.exists("ruirony_model"):
    messagebox.showerror("Ошибка", "Папка 'ruirony_model' с обученной моделью не найдена. Сначала обучите модель.")
    exit()

# Загрузка модели и токенизатора
model = BertForSequenceClassification.from_pretrained("ruirony_model")
tokenizer = BertTokenizer.from_pretrained("ruirony_model")
model.eval()

# Функция классификации текста
def classify():
    text = entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Пусто", "Введите текст для анализа")
        return
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        pred = torch.argmax(probs).item()
        confidence = probs[0][pred].item() * 100
        label = "Ирония" if pred == 1 else "Не ирония"
        result_label.config(text=f"{label} ({confidence:.2f}% уверенности)")

# Интерфейс
root = tk.Tk()
root.title("Распознавание иронии")
root.geometry("500x300")

entry = tk.Text(root, height=6, width=60)
entry.pack(pady=10)

button = tk.Button(root, text="Распознать", command=classify)
button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
