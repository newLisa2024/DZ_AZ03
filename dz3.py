from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import matplotlib.pyplot as plt
import re

# Создаем экземпляр веб-драйвера
driver = webdriver.Chrome()

try:
    # Открываем страницу с товарами на сайте
    driver.get("https://www.divan.ru/category/divany-i-kresla")

    # Даем странице время на загрузку
    time.sleep(5)

    # Прокручиваем страницу до конца, чтобы все элементы загрузились
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Добавляем задержку, чтобы дать время на загрузку новых элементов
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Ищем элементы, содержащие цены
    prices = driver.find_elements(By.XPATH, "//span[@data-testid='price']")

    if not prices:
        print("Цены не найдены.")
    else:
        print(f"Найдено {len(prices)} цен.")

    # Сохраняем найденные цены в список, убираем "₽" и пробелы, затем преобразуем в целые числа
    price_list = []
    for price in prices:
        price_text = price.text
        print(f"Обработка цены: {price_text}")
        price_text = re.sub(r'[^\d]', '', price_text)
        if price_text.isdigit():
            price_list.append(int(price_text))

    if not price_list:
        print("Цены не удалось обработать.")
    else:
        print(f"Обработано {len(price_list)} цен.")

    # Записываем цены в CSV файл
    with open('prices.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Price"])  # Записываем заголовок
        for price in price_list:
            writer.writerow([price])

    print("Цены успешно сохранены в файл prices.csv")

finally:
    # Закрываем браузер
    driver.quit()

    # Выводим цены
    print(price_list)

    # Строим гистограмму
    if price_list:
        plt.figure(figsize=(10, 6))
        plt.hist(price_list, bins=20, edgecolor='black')
        plt.title('Распределение цен на диваны и кресла')
        plt.xlabel('Цена (в рублях)')
        plt.ylabel('Количество товаров')
        plt.grid(True)
        plt.show()



