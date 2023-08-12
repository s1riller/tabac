from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def search_and_save_images(search_query, output_file):
    try:
        driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # Укажите путь к chromedriver

        # Открыть Яндекс
        driver.get('https://yandex.ru/images/')

        # Найти поле ввода запроса и ввести поисковый запрос
        search_input = driver.find_element(By.CSS_SELECTOR, '.input__control')
        search_input.send_keys(search_query)
        search_input.send_keys(Keys.RETURN)

        # Подождать пока загрузится страница результатов
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'serp-item')))

        # Получить ссылки на изображения
        images = driver.find_elements(By.CSS_SELECTOR, '.serp-item__link')
        image_links = [img.get_attribute('href') for img in images]

        # Записать ссылки в файл
        with open(output_file, 'w') as file:
            json.dump(image_links, file)

    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    product_name = 'название товара'  # Замените на реальное название товара
    output_file = 'product_images.json'  # Имя файла для сохранения ссылок на изображения

    search_and_save_images(product_name, output_file)
