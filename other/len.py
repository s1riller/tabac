import json

def count_products_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            num_products = len(data)
            return num_products
    except FileNotFoundError:
        return 0

if __name__ == "__main__":
    file_path = "vape_liquid_products.json"
    num_products = count_products_in_file(file_path)
    print(f"Количество товаров в файле {file_path}: {num_products}")
