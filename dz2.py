import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x_data = np.random.rand(100)  # 100 случайных чисел для оси x
y_data = np.random.rand(100)  # 100 случайных чисел для оси y

# Создание диаграммы рассеяния
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, alpha=0.7, edgecolors='b')
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X Данные')
plt.ylabel('Y Данные')
plt.grid(True)
plt.show()
