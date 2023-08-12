import requests
import json

def search_vape_liquid_products(access_token, sessionid_value):
    url = "https://lbe.litebox.ru/api/v1/gwares?page=0&limit=4322"

    headers = {
        "Authorization": access_token,
        "Accept": "application/json",
        "Cookie": f"sessionid={sessionid_value}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        vape_liquid_products = []

        for item in data.get("data", []):
            if "жидкость" in item.get("name", "").lower():
                vape_liquid_products.append(item)

        return vape_liquid_products
    else:
        print("Ошибка при выполнении запроса:", response.status_code)
        return []

def save_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    access_token = "4d99e3d6e19f48086f9fe81d14faa106013b6d19"
    sessionid_value = "jxr6xni1nghxz1tljkd0ud6vmnunk4un"
    vape_liquid_products = search_vape_liquid_products(access_token, sessionid_value)

    if vape_liquid_products:
        save_to_file(vape_liquid_products, "vape_liquid_products.json")
        print("Товары связанные с жидкостью для вейпов сохранены в файл vape_liquid_products.json")
    else:
        print("Нет данных о товарах связанных с жидкостью для вейпов")
