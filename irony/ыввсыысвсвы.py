import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score, precision_recall_curve, auc, brier_score_loss
import matplotlib.gridspec as gridspec
import seaborn as sns

# Настройки визуализации для улучшения читаемости
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 14


def plot_roc_curve(y_true, y_prob, ax):
    """Строит ROC-кривую."""
    fpr, tpr, thresholds = roc_curve(y_true, y_prob)
    roc_auc = roc_auc_score(y_true, y_prob)
    ax.plot(fpr, tpr, label='ROC-кривая (area = %0.3f)' % roc_auc)
    ax.plot([0, 1], [0, 1], 'k--')
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('Доля ложных срабатываний')
    ax.set_ylabel('Доля истинных срабатываний')
    ax.set_title('Рабочая характеристика приемника(ROC-кривая)')
    ax.legend(loc="lower right")


def plot_precision_recall_curve(y_true, y_prob, ax):
    """Строит Precision-Recall кривую."""
    precision, recall, thresholds = precision_recall_curve(y_true, y_prob)
    pr_auc = auc(recall, precision)
    ax.plot(recall, precision, label='PR-кривая (area = %0.3f)' % pr_auc)
    ax.set_xlabel('Полнота')
    ax.set_ylabel('Точность')
    ax.set_title('Кривая точности-полноты')
    ax.legend(loc="lower left")


def plot_gain_curve(y_true, y_prob, ax):
    """Строит Gain-кривую."""
    # Сортировка вероятностей и соответствующих истинных значений
    desc_score_indices = np.argsort(y_prob)[::-1]
    y_prob_sorted = y_prob[desc_score_indices]
    y_true_sorted = y_true[desc_score_indices]

    # Вычисление кумулятивного количества положительных примеров
    cumulative_positives = np.cumsum(y_true_sorted)
    total_positives = np.sum(y_true)
    # Вычисление Gain
    gain = cumulative_positives / total_positives

    # Вычисление идеального Gain (если бы мы идеально ранжировали)
    num_samples = len(y_true)
    ideal_gain = np.minimum(1, np.cumsum(np.ones(total_positives)) / total_positives)
    ideal_gain = np.concatenate([ideal_gain, np.ones(num_samples - total_positives)])

    # Построение графика
    ax.plot(np.linspace(0, 1, num_samples), gain, label='Прирост модели')
    ax.plot(np.linspace(0, 1, num_samples), ideal_gain, linestyle='--', color='green', label='Идеальный прирост')
    ax.plot(np.linspace(0, 1, num_samples), np.linspace(0, 1, num_samples), linestyle=':', color='gray', label='Случайный прирост') # Baseline

    ax.set_xlabel('Доля образцов')
    ax.set_ylabel('Прирост')
    ax.set_title('Кривая прироста')
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.legend(loc='lower right')


def main():
    # 1. Генерация синтетических данных (замените на свои реальные данные)
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # 2. Обучение модели (пример с Logistic Regression)
    model = LogisticRegression(solver='liblinear', random_state=42)  #solver важно указать
    model.fit(X_train, y_train)

    # 3. Получение вероятностей предсказаний
    y_prob = model.predict_proba(X_test)[:, 1]  # Вероятности для класса 1

    # 4. Визуализация
    fig = plt.figure(figsize=(20, 15)) #увеличил размер фигуры
    gs = gridspec.GridSpec(2, 2) #задал параметры сетки
    ax_roc = plt.subplot(gs[0, 0])
    ax_pr = plt.subplot(gs[0, 1])
    ax_gain = plt.subplot(gs[1, 0])
    ax_calib = plt.subplot(gs[1, 1])


    plot_roc_curve(y_test, y_prob, ax_roc)
    plot_precision_recall_curve(y_test, y_prob, ax_pr)
    plot_gain_curve(y_test, y_prob, ax_gain)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
