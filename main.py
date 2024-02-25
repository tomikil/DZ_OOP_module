from src.category import Category
from src.product import Product
import src.utils as utils

file = 'products.json'

conect = utils.filling_classes(utils.connection_file(file))

conect[0].add_product(Product.create_products({"name": "Xiaomi Redmi Note 11",
                                               "description": "1024GB, Синий",
                                               "price": 31000.0,
                                               "quantity": 4
                                               }, conect[0]))

print(conect[0].products)
