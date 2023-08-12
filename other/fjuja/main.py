import requests

# Замените на ваш реальный токен
token = "v1.71788.i5HcfeSP1ww3pO6SCeSxJ0nVcc3BQN2i389fldJeRlOgqczIXBYVfjWtYD7KoNS5"

# URL для запроса информации о заказе
url = f"https://www.botobot.ru/api/v1/getOrderInfo/{token}"

# Параметры запроса (в данном случае, передаем идентификатор заказа)
params = {
    "order_id": 12345  # Замените на нужный вам идентификатор заказа
}

# Отправка POST запроса
response = requests.post(url, json=params)

# Обработка ответа
if response.status_code == 200:
    data = response.json()
    if data["status"] == "success":
        order_info = data["data"]
        print("Информация о заказе:")
        print("ID заказа:", order_info["id"])
        print("Получатель:", order_info["recipient"])
        print("Адрес доставки:", order_info["address"])
        # ... и так далее, выведите необходимые данные
    else:
        print("Ошибка при получении информации о заказе:", data.get("message"))
else:
    print("Ошибка при выполнении запроса:", response.status_code)
