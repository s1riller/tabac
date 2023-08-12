import requests
import pandas as pd

def get_and_save_data(url, access_token, sessionid_value, output_file):
    headers = {
        "Authorization": access_token,
        "Accept": "application/json",
        "Cookie": f"sessionid={sessionid_value}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        df = pd.json_normalize(data['data'])  # Преобразование JSON данных в DataFrame
        df.to_excel(output_file, index=False)  # Сохранение DataFrame в Excel файл
        print("Данные успешно сохранены в", output_file)
    else:
        print("Ошибка при выполнении запроса:", response.status_code)

# Пример использования
access_token = "4d99e3d6e19f48086f9fe81d14faa106013b6d19"
sessionid_value = "jxr6xni1nghxz1tljkd0ud6vmnunk4un"
url = "https://lbe.litebox.ru/api/v1/waresgroup?page=0&limit=100"
output_file = "data.xlsx"

get_and_save_data(url, access_token, sessionid_value, output_file)
