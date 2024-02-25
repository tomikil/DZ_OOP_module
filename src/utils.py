import json
from src.product import Product
from src.category import Category


def connection_file(f):
    with open(f, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def filling_classes(file):
    category = []

    for item in file:
        product = []
        for prod in item['products']:
            product.append(Product(prod['name'], prod['description'], prod['price'], prod['quantity']))
        category.append(Category(item['name'], item['description'], product))

    return category
