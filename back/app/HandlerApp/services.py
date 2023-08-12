import requests
import re
# Импорт ваших моделей ProductGroup и Products
from .models import ProductGroup, Products, Products1
from datetime import datetime

current_date = datetime.now()
formatted_date = current_date.strftime('%d.%m.%Y')


def save_product_groups(url, access_token, sessionid_value):
    headers = {
        "Authorization": access_token,
        "Accept": "application/json",
        "Cookie": f"sessionid={sessionid_value}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for item in data.get('data', []):
            # Замените на актуальное имя поля
            product_group_name = item.get('product_group_name')
            product_group, created = ProductGroup.objects.get_or_create(
                wg_id=item['wg_id'],
                defaults={
                    'code': item['code'],
                    'name': item['name'],
                    'higher_id': item['higher_id'],
                    'external_id': item['external_id'],
                    'external_code': item['external_code'],
                }
            )
            product, created = Products.objects.get_or_create(
                code=item['code'],
                name=item['name'],
                # ... Остальные поля для создания Products
                product_group=product_group  # Установите значение связанного поля
            )
            if created:
                print(f"Создана запись группы: {product_group}")
            else:
                print(f"Запись группы уже существует: {product_group}")
    else:
        print("Ошибка при выполнении запроса:", response.status_code)


def save_products(url, access_token, sessionid_value):
    headers = {
        "Authorization": access_token,
        "Accept": "application/json",
        "Cookie": f"sessionid={sessionid_value}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for item in data.get('data', []):
            product, created = Products.objects.get_or_create(
                wares_id=item['wares_id'],
                defaults={
                    'code': item['code'],
                    'name': item['name'],
                    'full_name': item['full_name'],
                    'wareskind_code': item['wareskind_code'],
                    'main_unit_id': item['main_unit_id'],
                    'wg_id': item['wg_id'],
                    'producer_id': item.get('producer_id'),
                    'importer_id': item.get('importer_id'),
                    'tax_id': item['tax_id'],
                    'alccode': item.get('alccode'),
                    'wares_parent': item['wares_parent'],
                    'wares_parent_id': item.get('wares_parent_id'),
                    'wares_type_code': item['wares_type_code'],
                    'country_code': item['country_code'],
                    'country_name': item['country_name'],
                    'volume_value': item['volume_value'],
                    'proof_value': item['proof_value'],
                    'external_id': item['external_id'],
                    'external_code': item.get('external_code'),
                    'wares_views_code': item.get('wares_views_code'),
                    'status': item.get('status'),
                    'status_name': item.get('status_name'),
                    'wares_type_name': item.get('wares_type_name'),
                }
            )
            if created:
                print(f"Создана запись товара: {product}")
            else:
                print(f"Запись товара уже существует: {product}")
    else:
        print("Ошибка при выполнении запроса:", response.status_code)


def extract_barcodes(data):
    barcodes = [item['barcode'] for item in data]
    barcodes_str = '\n'.join(barcodes)
    return barcodes_str


def save_products1(url, access_token, sessionid_value):
    headers = {
        "Authorization": access_token,
        "Accept": "application/json",
        "Cookie": f"sessionid={sessionid_value}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for item in data.get('data', []):
            # Retrieve the corresponding ProductGroup instance
            try:
                product_group = ProductGroup.objects.get(wg_id=item['wg_id'])
            except ProductGroup.DoesNotExist:
                product_group = None

            # Извлечение и обработка баркодов
            barcode = save_numeric_barcodes(item.get('barcodes', []))

            product, created = Products1.objects.get_or_create(
                id=item['code'],
                defaults={
                    'name': item['full_name'],
                    'wares_id': item.get("wares_id"),
                    'barcode': barcode,
                    'group': item['wareskind_code'],
                    'unit': 'шт' if item['main_unit_id'] == 55 else item['main_unit_id'],
                    'image': item.get('image'),
                    'group': product_group,  # Assign the retrieved ProductGroup instance
                }
            )
            # if created:
            #     print(f"Создана запись товара: {product.name}")
            # else:
            #     print(f"Запись товара уже существует: {product}")
    else:
        print("Ошибка при выполнении запроса:", response.status_code)


def save_sale_prices(url, access_token, sessionid_value):
    headers = {
        "Authorization": access_token,
        "Accept": "application/json",
        "Cookie": f"sessionid={sessionid_value}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # print(data)
        for item in data.get('data', []):
            try:
                # Обратите внимание на использование ключа 'wares_id'
                product = Products1.objects.get(wares_id=item['wares_id'])
                product.price = item['sale_price']
                product.save()
                # print(f"Цена товара с wares_id {item['wares_id']} обновлена: {product.price}")
            except Products1.DoesNotExist:
                print(f"Товар с wares_id {item['wares_id']} не найден.")
    else:
        print("Ошибка при выполнении запроса:", response.status_code)


def delete_all_products():
    Products1.objects.all().delete()
    print("Все товары были удалены.")


def save_numeric_barcodes(data):
    barcode_values = []
    has_numeric_barcode = False

    for item in data:
        if 'barcode' in item and item['barcode'] is not None:
            barcode = item['barcode']
            if barcode == 'none':
                barcode_values.append('none')
            else:
                numeric_values = re.findall(r'\d+', barcode)
                if numeric_values:
                    barcode_values.extend(numeric_values)
                    has_numeric_barcode = True

    if has_numeric_barcode:
        return '\n'.join(barcode_values)
    else:
        return 'none'


def update_barcodes():
    products = Products1.objects.all()
    for product in products:
        barcode_list = []
        if product.barcode:
            if isinstance(product.barcode, str) and product.barcode.isdigit():
                barcode_list.append(product.barcode)
            else:
                barcode_list.append('none')
        new_barcode = '\n'.join(barcode_list)
        product.barcode = new_barcode
        product.save()
    print("Штрих-коды Обновлены")


def save_quantity(url, access_token, sessionid_value):
    headers = {
        "Authorization": access_token,
        "Accept": "application/json",
        "Cookie": f"sessionid={sessionid_value}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        for item in data.get('data', []):
            try:
                # Обратите внимание на использование ключа 'wares_id'
                product = Products1.objects.get(wares_id=item['wares_id'])
                product.quantity = item['quantity']
                product.save()
                # print(f"Цена товара с wares_id {item['wares_id']} обновлена: {product.price}")
            except Products1.DoesNotExist:
                print(f"Товар с wares_id {item['wares_id']} не найден.")
        print("Количество сохранено")
    else:
        print("Ошибка при выполнении запроса:", response.status_code)


access_token = "4d99e3d6e19f48086f9fe81d14faa106013b6d19"
sessionid_value = "jxr6xni1nghxz1tljkd0ud6vmnunk4un"
group_url = "https://lbe.litebox.ru/api/v1/waresgroup?page=0&limit=500"
product_url = "https://lbe.litebox.ru/api/v1/gwares?page=0&limit=5000"
url_for_get_sale = "https://lbe.litebox.ru/api/v1/object/43/saleprice"
url_for_get_quantity = f"https://lbe.litebox.ru/api/v1/object/43/waresrest?restdate={formatted_date}"


def run():
    save_product_groups(group_url, access_token, sessionid_value)
    # save_products(product_url, access_token, sessionid_value)
    delete_all_products()
    save_products1(product_url, access_token, sessionid_value)
    save_sale_prices(url_for_get_sale, access_token, sessionid_value)
    save_quantity(url_for_get_quantity, access_token, sessionid_value)
    update_barcodes()
    print("Все ОК")
