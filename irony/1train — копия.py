import pandas as pd
from sklearn.model_selection import train_test_split
from datasets import Dataset
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import torch
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

TRAINING_FILE = "ruirony_combined_unique.csv"
MODEL_DIR = "ruirony_model"

# Загрузка данных
if not os.path.exists(TRAINING_FILE):
    raise FileNotFoundError(f"Файл {TRAINING_FILE} не найден.")

df = pd.read_csv(TRAINING_FILE).dropna()
df["label"] = df["label"].astype(int)

if len(df) < 10:
    raise ValueError("Недостаточно данных для обучения. Нужно хотя бы 10 примеров.")

train_texts, val_texts, train_labels, val_labels = train_test_split(
    df["text"].tolist(), df["label"].tolist(), test_size=0.2, random_state=42
)

# Инициализация модели и токенизатора
model_name = "sberbank-ai/ruBert-base"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)

def tokenize(batch):
    return tokenizer(batch["text"], padding="max_length", truncation=True, max_length=128)

train_dataset = Dataset.from_dict({"text": train_texts, "label": train_labels}).map(tokenize).remove_columns(["text"])
val_dataset = Dataset.from_dict({"text": val_texts, "label": val_labels}).map(tokenize).remove_columns(["text"])

def compute_metrics(p):
    preds = torch.argmax(torch.tensor(p.predictions), axis=1)
    labels = torch.tensor(p.label_ids)
    acc = accuracy_score(labels, preds)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average="binary")
    return {"accuracy": acc, "precision": precision, "recall": recall, "f1": f1}

args = TrainingArguments(
    output_dir=MODEL_DIR,
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=5,
    weight_decay=0.01,
    save_total_limit=1,
    load_best_model_at_end=False,
    logging_dir="./logs",
    logging_steps=10,
    report_to="none",
    disable_tqdm=False
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    compute_metrics=compute_metrics
)

trainer.train()
model.save_pretrained(MODEL_DIR)
tokenizer.save_pretrained(MODEL_DIR)
import matplotlib.pyplot as plt

# График изменения метрик по эпохам
metrics = trainer.state.log_history
train_loss = [m["loss"] for m in metrics if "loss" in m and "epoch" in m]
eval_f1 = [m["eval_f1"] for m in metrics if "eval_f1" in m and "epoch" in m]
epochs = list(range(1, len(train_loss)+1))

plt.figure(figsize=(10, 5))
plt.plot(epochs, train_loss, label="Train Loss", marker='o')
if len(eval_f1) == len(epochs):
    plt.plot(epochs, eval_f1, label="Eval F1", marker='x')
else:
    print("⚠️ Предупреждение: количество точек eval_f1 не совпадает с количеством эпох. График f1 не будет построен.")
plt.title("Динамика обучения модели")
plt.xlabel("Эпоха")
plt.ylabel("Значение")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("training_metrics.png")
plt.close()

print("✅ Обучение завершено. Модель сохранена в папку 'ruirony_model'.")
print("📈 График сохранён как 'training_metrics.png'.")
