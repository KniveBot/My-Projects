import tkinter as tk
from tkinter import messagebox
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Загрузка модели и токенизатора
tokenizer = BertTokenizer.from_pretrained("sberbank-ai/ruBert-base")
model = BertForSequenceClassification.from_pretrained("sberbank-ai/ruBert-base", num_labels=2)
model.eval()

# Функция предсказания
def predict_irony(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    prediction = torch.argmax(probs, dim=1).item()
    confidence = probs[0][prediction].item() * 100
    return prediction, confidence

# GUI
def run_gui():
    def on_submit():
        user_input = entry.get("1.0", tk.END).strip()
        if not user_input:
            messagebox.showwarning("Ошибка", "Введите текст для анализа.")
            return
        label, conf = predict_irony(user_input)
        result = "Ирония" if label == 1 else "Не ирония"
        result_label.config(text=f"Результат: {result} (уверенность: {conf:.2f}% уверенности)")

    window = tk.Tk()
    window.title("Определение иронии в тексте")
    window.geometry("450x300")
    window.configure(bg="dark blue")

    tk.Label(window, text="Введите текст для анализа:", bg="dark blue", fg="white").pack(pady=5)
    entry = tk.Text(window, height=6, wrap='word')
    entry.pack(padx=10, pady=5)

    tk.Button(window, text="Распознать", command=on_submit, bg="light blue").pack(pady=10)
    result_label = tk.Label(window, font=("Arial", 12), bg="dark blue", fg="white")
    result_label.pack(pady=10)

    window.mainloop()

run_gui()
