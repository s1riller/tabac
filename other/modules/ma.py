import requests

# Предполагается, что у вас уже есть Access токен
access_token = "4d99e3d6e19f48086f9fe81d14faa106013b6d19"
sessionid_value = "jxr6xni1nghxz1tljkd0ud6vmnunk4un"

# URL защищенного ресурса API, который требует авторизацию
url = "https://lbe.litebox.ru/api/v1/gwares?page=0&limit=2"

# Заголовки запроса с токеном авторизации
headers = {
    "Authorization": access_token,
    "Accept": "application/json",
    "Cookie": f"sessionid={sessionid_value}"
}

# Выполняем GET запрос к защищенному ресурсу API
response = requests.get(url, headers=headers)

# Обрабатываем ответ
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Ошибка при выполнении запроса:", response.status_code)
